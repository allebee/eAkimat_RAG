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
from app.agent.tools.db_query import query_database
from app.agent.tools.knowledge_base import search_knowledge_base
from app.config import settings
from app.knowledge.context_mapping import get_page_label

logger = logging.getLogger(__name__)

# All available tools
ALL_TOOLS = [
    search_knowledge_base,
    query_database,
]


class AgentState(TypedDict):
    """State schema for the LangGraph agent."""

    messages: Annotated[List[BaseMessage], add_messages]
    context_page: str
    language: str


def _build_llm():
    """Create the LLM instance with tool bindings.

    Uses xAI Grok via OpenAI-compatible API.
    """
    llm = ChatOpenAI(
        model=settings.grok_model,
        api_key=settings.grok_api_key,
        base_url=settings.grok_base_url,
        temperature=0.1,
        streaming=True,
    )
    return llm.bind_tools(ALL_TOOLS)


def _agent_node(state: AgentState) -> Dict[str, Any]:
    """Main agent node — invokes the LLM with tools."""
    llm = _build_llm()
    response = llm.invoke(state["messages"])
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
