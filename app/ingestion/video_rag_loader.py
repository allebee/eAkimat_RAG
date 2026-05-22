"""Video RAG loader — ingests pre-processed _rag.json transcription files.

Each JSON file contains an array of chunks with:
  - source_file: original video filename
  - start_time / end_time: timestamps in seconds
  - topic: topic label
  - clean_text: cleaned transcription text
  - screenshot: relative path to the frame image
"""

from __future__ import annotations

import hashlib
import json
import logging
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.config import settings

logger = logging.getLogger(__name__)

# Minimum text length for a useful chunk
MIN_CHUNK_LENGTH = 30


def _sanitize_filename(name: str) -> str:
    """Create a safe filename from potentially problematic characters."""
    # Replace problematic chars but keep Cyrillic
    for ch in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
        name = name.replace(ch, '_')
    return name


def _generate_id(source_file: str, chunk_idx: int) -> str:
    """Generate a deterministic document ID for a video chunk."""
    raw = f"video_{source_file}_chunk_{chunk_idx}"
    return f"video_{hashlib.md5(raw.encode()).hexdigest()}"


def load_video_rag_json(
    json_path: Path,
    frames_source_dir: Path,
    frames_target_dir: Path,
) -> List[Dict[str, Any]]:
    """Load a single _rag.json file and return documents ready for ChromaDB.

    Args:
        json_path: Path to the _rag.json file.
        frames_source_dir: Directory containing the source frame JPGs.
        frames_target_dir: Target directory to copy frames to (for serving).

    Returns:
        List of dicts with 'id', 'content', and 'metadata'.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            chunks = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        logger.warning("Failed to load %s: %s", json_path, e)
        return []

    if not isinstance(chunks, list):
        logger.warning("Expected list in %s, got %s", json_path, type(chunks).__name__)
        return []

    documents: List[Dict[str, Any]] = []

    for idx, chunk in enumerate(chunks, 1):
        clean_text = chunk.get("clean_text", "").strip()
        if len(clean_text) < MIN_CHUNK_LENGTH:
            continue

        source_file = chunk.get("source_file", json_path.stem)
        topic = chunk.get("topic", "")
        start_time = chunk.get("start_time", 0)
        end_time = chunk.get("end_time", 0)
        screenshot_rel = chunk.get("screenshot", "")

        # Process screenshot
        image_marker = ""
        if screenshot_rel:
            # The screenshot path in JSON is like:
            # "workspace/dataset/frames/VideoName.mp4_chunk_1.jpg"
            # We need the actual filename
            frame_filename = Path(screenshot_rel).name

            # Try to find and copy the frame
            source_frame = frames_source_dir / frame_filename
            if source_frame.exists():
                target_frame = frames_target_dir / frame_filename
                if not target_frame.exists():
                    try:
                        shutil.copy2(source_frame, target_frame)
                    except OSError as e:
                        logger.warning("Failed to copy frame %s: %s", frame_filename, e)

                # Use the video/ subdirectory prefix for serving
                image_marker = f"\n\n[IMAGE: video/{frame_filename}]"
            else:
                logger.debug("Frame not found: %s", source_frame)

        # Build content with screenshot marker inline
        content = clean_text + image_marker

        # Video title (without .mp4 extension)
        video_title = source_file.replace(".mp4", "")

        metadata: Dict[str, Any] = {
            "source_type": "video",
            "source_file": source_file,
            "video_title": video_title,
            "topic": topic,
            "start_time": start_time,
            "end_time": end_time,
            "chunk_index": idx,
            "has_screenshot": bool(image_marker),
        }

        doc_id = _generate_id(source_file, idx)

        documents.append({
            "id": doc_id,
            "content": content,
            "metadata": metadata,
        })

    return documents


def load_all_video_rag(
    video_dataset_dir: str,
    frames_target_dir: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Load all _rag.json files from the video dataset directory.

    Args:
        video_dataset_dir: Path to the output_dataset directory.
        frames_target_dir: Where to copy frames for serving. 
                          Defaults to storage/images/video/.

    Returns:
        List of all documents from all video files.
    """
    dataset_dir = Path(video_dataset_dir)
    if not dataset_dir.exists():
        logger.warning("Video dataset directory not found: %s", dataset_dir)
        return []

    # Source frames directory
    frames_source = dataset_dir / "frames"
    if not frames_source.exists():
        logger.warning("Frames directory not found: %s", frames_source)
        frames_source = dataset_dir  # Fallback

    # Target directory for serving frames
    if frames_target_dir:
        target_dir = Path(frames_target_dir)
    else:
        target_dir = settings.images_path / "video"
    target_dir.mkdir(parents=True, exist_ok=True)

    # Find all _rag.json files
    rag_files = sorted(dataset_dir.glob("*_rag.json"))
    logger.info("Found %d _rag.json files in %s", len(rag_files), dataset_dir)

    all_docs: List[Dict[str, Any]] = []
    for rag_file in rag_files:
        docs = load_video_rag_json(rag_file, frames_source, target_dir)
        all_docs.extend(docs)
        if docs:
            logger.info("  %s → %d chunks", rag_file.name, len(docs))

    logger.info("Total video RAG documents: %d", len(all_docs))
    return all_docs
