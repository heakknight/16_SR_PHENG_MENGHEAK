"""
Step 4 : Check that the vector store can retrieve relevant chunks.
"""

from app.embeddings import embed_query
from app.vector_store import get_collection


def main():
    question = input("Enter your question: ")

    query_vector = embed_query(question)

    collection = get_collection()

    results = collection.query(query_embeddings=[query_vector], n_results=3)

    print(f"\nQuestion: {question}")
    print("\nTop 3 retrieved chunks:\n")

    documents = results.get("documents")
    metadatas = results.get("metadatas")

    if not documents or not metadatas:
        print("No results found.")
        return

    documents = documents[0]
    metadatas = metadatas[0]

    for i, (document, metadata) in enumerate(
        zip(documents, metadatas),
        start=1,
    ):
        print(f"--- Result {i} ---")
        print(f"Source: {metadata['source']}")
        print(f"Chunk: {metadata['chunk_index']}")
        print(f"Content:\n{document}")
        print()

if __name__ == "__main__":
    main()