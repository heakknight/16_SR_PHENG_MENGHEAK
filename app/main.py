"""
Step 6 : Terminal chat interface for the RAG application.
"""

from app.pipeline import answer_question

def main():
  print("RAG Chatbot")
  print("Type 'exit' to quit.\n")

  while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question:
        continue

    answer = answer_question(question)

    print(f"\nAssistant: {answer}\n")

if __name__ == "__main__":
    main()