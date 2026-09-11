"""
Step 1 : Load source documents from the data directory.
"""

import os
from typing import List, Tuple

from chromadb.config import Settings
from pypdf import PdfReader

from app.config import DATA_DIR
from app.embeddings import embed_texts

def __read_text(path: str) -> str:
  with open(path, "r", encoding="utf-8") as f:
    return f.read()

def __read_pdf(path: str) -> str:
  reader = PdfReader(path)

  return "\n".join(page.extract_text() or "" for page in reader.pages)

def load_documents(data_dir: str = DATA_DIR) -> List[Tuple[str, str]]:
  documents = []
  for filename in sorted(os.listdir(data_dir)):
    path = os.path.join(data_dir, filename)
    if not os.path.isfile(path):
      continue
    ext = filename.lower().rsplit(".", 1)[-1]
    if ext in ("txt", "md"):
      content = __read_text(path)
    elif ext == "pdf":
      content = __read_pdf(path)
    else:
      continue
    if content.strip():
      documents.append((filename, content))
  return documents