"""
Step 3 : Index document chunks and their embeddings in ChromaDB.
"""

import chromadb
from chromadb.config import Settings
from app.config import CHROMA_DB_DIR, COLLECTION_NAME, DATA_DIR
from app.ingestion import load_documents
from app.chunking import chunk_text
from app.embeddings import embed_texts

def get_collection():
  client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
  return client.get_or_create_collection(name=COLLECTION_NAME)

def build_index(data_dir: str = DATA_DIR) -> int:
  """
  Build a vector index from the documents in data_dir.

  Loads documents, splits them into chunks, creates embeddings,
  and stores the chunks, embeddings, and metadata in ChromaDB.
  The existing collection is replaced, and the number of indexed
  chunks is returned.
  """
  client = chromadb.PersistentClient(path= CHROMA_DB_DIR)
  try:
    client.delete_collection(COLLECTION_NAME)
  except:
    pass
  collection = client.get_or_create_collection(name= COLLECTION_NAME)

  documents = load_documents(data_dir)
  if not documents:
    raise FileNotFoundError(f"No .txt/.md/.pdf files that found in '{data_dir}/'")
  
  ids, texts, metadatas = [], [], []
  for filename, full_text in documents:
    for i, chunk in enumerate(chunk_text(full_text)):
      ids.append(f"{filename}::{i}")
      texts.append(chunk)
      metadatas.append({"source": filename, "chunk_index":i})

  embeddings = embed_texts(texts)
  collection.add(ids=ids, documents=texts, embeddings=embeddings, metadatas=metadatas)  # type: ignore
  return len(texts)

if __name__ == "__main__":
    count = build_index()
    print(f"Indexed {count} chunks from '{DATA_DIR}/' into Chroma at '{CHROMA_DB_DIR}/'") 