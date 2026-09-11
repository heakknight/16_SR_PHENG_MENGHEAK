# Step 7: Test Log

I tested the RAG application with 5 questions. Four questions were related to
the documents, and one question was outside the documents.

## Test 1

**Question:**  
What HTTP method is used to create a new resource, and which status code indicates success?

**Retrieved chunks:**
- `rest_api_guide.txt` — Chunk 1
- `rag_application.txt` — Chunk 5
- `rest_api_guide.txt` — Chunk 2

**Answer:**

POST is commonly used to create a new resource.

A status code of 201 means that a resource was successfully created.

---

## Test 2

**Question:**  
Why is overlap used when splitting documents into chunks?

**Retrieved chunks:**
- `rag_application.txt` — Chunk 2
- `rag_application.txt` — Chunk 1
- `rag_application.txt` — Chunk 7

**Answer:**

Overlap helps preserve information when an important sentence is close to a
chunk boundary.

---

## Test 3

**Question:**  
Why should a developer use a `with` statement when reading a file in Python?

**Retrieved chunks:**
- `python_development_guide.txt` — Chunk 2
- `python_development_guide.txt` — Chunk 1
- `python_development_guide.txt` — Chunk 3

**Answer:**

A `with` statement is used when reading a file so that the file is closed
automatically after reading.

---

## Test 4

**Question:**  
What metadata can be stored alongside embeddings in a vector database?

**Retrieved chunks:**
- `rag_application.txt` — Chunk 3
- `rag_application.txt` — Chunk 4
- `rag_application.txt` — Chunk 7

**Answer:**

The metadata can include:

- source filename
- chunk index
- document type

---

## Test 5

**Question:**  
What is the capital city of France and what is its official currency?

**Retrieved chunks:**
- `rag_application.txt` — Chunk 4
- `rag_application.txt` — Chunk 3
- `python_development_guide.txt` — Chunk 2

**Answer:**

I don't have enough information in the documents to answer that.