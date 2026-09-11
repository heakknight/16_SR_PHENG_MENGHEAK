"""
One function, one job: turn text into vectors using the local Ollama
embedding model. nomic-embed-text
Both ingestion (embedding chunks) and retrieval
(embedding the user's question) call this, so the two are guaranteed
to use the same model and never drift apart.
"""
from typing import List

import ollama

from app.config import EMBED_MODEL


def embed_texts(texts: List[str]) -> List[List[float]]:
    """Convert multiple text strings into embedding vectors."""
    if not texts:
        return []
    response = ollama.embed(model=EMBED_MODEL, input=texts)
    return list(response.embeddings) # type:ignore


def embed_query(text: str) -> List[float]:
    """Convert one user query into a single embedding vector."""
    return embed_texts([text])[0] 