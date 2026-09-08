"""Central configuration settings for the RAG application."""

EMBED_MODEL = "nomic-embed-text"
GEN_MODEL = "qwen3:4b"

DATA_DIR = "data"
CHROMA_DB_DIR = "chroma_db"
COLLECTION_NAME = "documents"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 120

TOP_K = 4

SYSTEM_PROMPT = (
    "You are a helpful assistant that answers questions using ONLY the "
    "context provided below. If the answer is not contained in the context, "
    "say \"I don't have enough information in the documents to answer that.\" "
    "Do not use outside knowledge or invent information. "
    "Cite only source file names explicitly included in the context."
)