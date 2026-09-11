"""
Step 5 : Connect retrieval and generation into one RAG pipeline.
"""

from app.retriever import retrieve
from app.generator import generate_answer


def answer_question(question: str) -> str:
  """
  Retrieve relevant chunks and generate a grounded answer.
  """

  chunks = retrieve(question)

  answer = generate_answer(
    question,
    chunks,
  )

  return answer