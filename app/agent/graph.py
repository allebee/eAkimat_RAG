"""LangGraph agent — routes queries between knowledge base and analytics."""

from __future__ import annotations

import logging
from typing import Annotated, Any, Dict, List, Optional, TypedDict

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from app.agent.prompts import build_system_prompt
from app.agent.tools.knowledge_base import search_knowledge_base
from app.config import settings
from app.knowledge.context_mapping import get_page_label

logger = logging.getLogger(__name__)

# All available tools
# NOTE: query_database (SQL analytics) is intentionally unbound for now — the
# analytics module is on hold. app/agent/tools/db_query.py is left untouched;
# re-add the import and this entry to switch it back on.
ALL_TOOLS = [
    search_knowledge_base,
]


class AgentState(TypedDict):
    """State schema for the LangGraph agent."""

    messages: Annotated[List[BaseMessage], add_messages]
    context_page: str
    language: str


# Cache the built LLM so all requests share one httpx connection pool to the
# provider (rebuilding per request would open a fresh pool each time and kill
# keep-alive under load).
_llm_cached = None


def _build_llm():
    """Create (once) the LLM instance with tool bindings.

    Provider (Grok or DeepSeek) is picked by LLM_PROVIDER — both speak the
    OpenAI-compatible API.
    """
    global _llm_cached
    if _llm_cached is None:
        llm = ChatOpenAI(
            model=settings.llm_model,
            api_key=settings.llm_api_key,
            base_url=settings.llm_base_url,
            temperature=0.1,
            streaming=True,
            timeout=90,       # DeepSeek can be slow on long answers
            max_retries=3,    # recover from transient stream drops (RemoteProtocolError)
        )
        _llm_cached = llm.bind_tools(ALL_TOOLS)
    return _llm_cached


async def _agent_node(state: AgentState) -> Dict[str, Any]:
    """Main agent node — invokes the LLM with tools.

    Async so the (multi-second) provider call runs on the event loop instead of
    blocking a threadpool thread — this is what lets many requests wait on the
    LLM concurrently.
    """
    llm = _build_llm()
    response = await llm.ainvoke(state["messages"])
    return {"messages": [response]}


def _should_continue(state: AgentState) -> str:
    """Route: if the last message has tool calls, go to tools. Otherwise, end."""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return END


def build_graph() -> StateGraph:
    """Build the LangGraph agent graph.

    Flow: agent → (tool calls?) → tools → agent → ... → END
    """
    tool_node = ToolNode(ALL_TOOLS)

    graph = StateGraph(AgentState)
    graph.add_node("agent", _agent_node)
    graph.add_node("tools", tool_node)

    graph.set_entry_point("agent")
    graph.add_conditional_edges("agent", _should_continue, {"tools": "tools", END: END})
    graph.add_edge("tools", "agent")

    return graph.compile()


# Compiled graph singleton
_compiled_graph = None


def get_graph():
    """Get or create the compiled agent graph."""
    global _compiled_graph
    if _compiled_graph is None:
        _compiled_graph = build_graph()
    return _compiled_graph


async def run_agent(
    message: str,
    context_page: Optional[str] = None,
    language: str = "ru",
    chat_history: Optional[List[BaseMessage]] = None,
) -> str:
    """Run the agent with a user message and return the text response.

    Args:
        message: User's question.
        context_page: Frontend page_id for contextual filtering.
        language: User's language preference.
        chat_history: Previous messages for multi-turn conversations.

    Returns:
        The agent's final text response.
    """
    graph = get_graph()

    # Build system prompt with context
    page_label = get_page_label(context_page, language) if context_page else ""
    system_prompt = build_system_prompt(
        page_label=page_label,
        page_id=context_page or "",
        language=language,
    )

    # Build message list
    messages: List[BaseMessage] = [SystemMessage(content=system_prompt)]
    if chat_history:
        messages.extend(chat_history)
    messages.append(HumanMessage(content=message))

    # Run the graph
    state: AgentState = {
        "messages": messages,
        "context_page": context_page or "",
        "language": language,
    }

    result = await graph.ainvoke(state)

    # Extract final AI response
    final_messages = result.get("messages", [])
    for msg in reversed(final_messages):
        if isinstance(msg, AIMessage) and msg.content:
            return msg.content

    return "Не удалось получить ответ. Пожалуйста, попробуйте позже."


async def stream_agent(
    message: str,
    context_page: Optional[str] = None,
    language: str = "ru",
    chat_history: Optional[List[BaseMessage]] = None,
):
    """Run the agent, yielding lifecycle events so the UI can show progress.

    Observes the graph's node transitions via ``astream(stream_mode="updates")``
    and maps them to human-facing stages. Yields dicts:

        {"kind": "status", "stage": "thinking" | "searching" | "generating"}
        {"kind": "answer", "content": <final answer text>}

    The final answer is yielded once, whole — callers keep doing the image-safe
    post-processing on it, so [IMAGE:] markers are never split mid-stream.
    """
    graph = get_graph()

    page_label = get_page_label(context_page, language) if context_page else ""
    system_prompt = build_system_prompt(
        page_label=page_label,
        page_id=context_page or "",
        language=language,
    )

    messages: List[BaseMessage] = [SystemMessage(content=system_prompt)]
    if chat_history:
        messages.extend(chat_history)
    messages.append(HumanMessage(content=message))

    state: AgentState = {
        "messages": messages,
        "context_page": context_page or "",
        "language": language,
    }

    # The first LLM call (deciding whether to use a tool) is the long silent
    # wait — announce it up front.
    yield {"kind": "status", "stage": "thinking"}

    final_answer = ""
    async for chunk in graph.astream(state, stream_mode="updates"):
        for node, update in chunk.items():
            node_msgs = (update or {}).get("messages", []) if isinstance(update, dict) else []
            if not node_msgs:
                continue
            last = node_msgs[-1]

            if node == "agent":
                if getattr(last, "tool_calls", None):
                    # Agent chose to look something up.
                    yield {"kind": "status", "stage": "searching"}
                elif getattr(last, "content", ""):
                    # Agent produced the final answer (no more tool calls).
                    final_answer = last.content
            elif node == "tools":
                # Search finished; the agent will now compose the answer.
                yield {"kind": "status", "stage": "generating"}

    if not final_answer:
        final_answer = "Не удалось получить ответ. Пожалуйста, попробуйте позже."
    yield {"kind": "answer", "content": final_answer}
