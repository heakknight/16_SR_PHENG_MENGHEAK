"""
Step 2 : Split source documents into smaller chunks for retrieval.
"""

from app.config import CHUNK_OVERLAP, CHUNK_SIZE

def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
  """
    Fixed size chuking with overlap
  """

  text = text.strip()
  if not text:
    return []
  chunks = []
  start = 0
  while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    if end >= len(text):
      break
    start = end - overlap
  return chunks