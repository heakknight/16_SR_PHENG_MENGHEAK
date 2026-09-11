"""
Step 5 : Generate a grounded answer using the local LLM.
"""

from typing import List
import ollama

from app.config import LLM_MODEL, SYSTEM_PROMPT
from app.retriever import RetrievedChunk

def build_prompt(query: str, chunks: List[RetrievedChunk]) -> str:
  """
    Build a prompt using the user's question and retrieved chunks.
  """
  if not chunks:
      context_block = "(no relevant context was found)"
  else:
    context_block = "\n\n".join(
        f"[{i + 1}] {c['source']}\n{c['text']}"
        for i, c in enumerate(chunks)
    )

  return (
    f"Context:\n{context_block}\n\n"
    f"Question:\n{query}\n\n"
    "Answer the question using only the information provided in the context above. "
    "If the context does not contain enough information to answer the question, "
    "say that you do not have enough information in the documents. "
    "Do not use outside knowledge or make up information."
  )

def generate_answer(query: str, chunks: List[RetrievedChunk]) -> str:
  prompt = build_prompt(query, chunks)
  response = ollama.chat(
    model=LLM_MODEL,
    messages=[
       {"role": "system", "content": SYSTEM_PROMPT},
       {"role": "user", "content": prompt}
    ]
  )
  return response.message.content #type:ignore