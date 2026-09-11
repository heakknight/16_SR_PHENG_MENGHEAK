# Baseline RAG Document Chat

A local Retrieval-Augmented Generation (RAG) application built with Python, Ollama, and ChromaDB. The application retrieves relevant information from local documents and uses a local language model to generate grounded answers with source citations.

---

## Technology Stack

* **Language:** Python 3.11+
* **Package Manager:** Poetry
* **LLM Provider:** Ollama (local server)
* **Embedding Model:** `nomic-embed-text` (via Ollama)
* **Generation Model:** `llama3.2:3b` (via Ollama)
* **Vector Database:** ChromaDB (persistent mode)
* **Document Processing:** `pypdf` and built-in Python file I/O

---

## Project Structure

```text
16_SR_PHENG_MENGHEAK/
├── app/
│   ├── __init__.py
│   ├── config.py             # Central application configuration and prompts
│   ├── ingestion.py          # Step 1: Loads documents (.txt, .md, .pdf) from data/
│   ├── chunking.py           # Step 2: Fixed-size text chunker with overlap
│   ├── embeddings.py         # Step 3: Embeds chunks and queries via Ollama
│   ├── vector_store.py       # Step 3: Indexes chunk vectors into ChromaDB
│   ├── demo_vector_check.py  # Step 4: Standalone test script for vector search
│   ├── retriever.py          # Step 5: Queries ChromaDB and returns top chunks
│   ├── generator.py          # Step 5: Constructs prompt and generates grounded answer
│   ├── pipeline.py           # Step 5: End-to-end RAG workflow facade
│   └── main.py               # Step 6: Terminal interactive chat loop
├── data/                     # Source documents
│   ├── python_development_guide.txt
│   ├── rag_application.txt
│   └── rest_api_guide.txt
├── chroma_db/                # Persistent ChromaDB storage directory
├── test_log.md               # Step 7: Complete evaluation test log (5 questions)
├── reflection.md             # Step 8: Written project reflection
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

## Project Components

Each module in `app/` has a single, well-defined responsibility:

1. **`app/config.py`**: Centralizes all configuration variables, including model names, data directories, chunking parameters, retrieval top-k, and system prompts.
2. **`app/ingestion.py`**: Reads raw text, Markdown, and PDF documents from the `data/` directory and returns filename-text pairs.
3. **`app/chunking.py`**: Splits continuous document texts into uniform chunks using a sliding window.
4. **`app/embeddings.py`**: Provides unified embedding functions (`embed_texts` and `embed_query`) via Ollama's `nomic-embed-text` model.
5. **`app/vector_store.py`**: Manages ChromaDB persistent collection initialization and builds the document vector index.
6. **`app/demo_vector_check.py`**: Standalone testing script that takes a user query, embeds it, queries ChromaDB, and displays the top-3 matching chunks with metadata.
7. **`app/retriever.py`**: Embeds incoming queries, retrieves the top `TOP_K` relevant chunks from ChromaDB, and packages them with distance and metadata.
8. **`app/generator.py`**: Formats retrieved context chunks into a grounded prompt and queries `llama3.2:3b` with strict anti-hallucination instructions.
9. **`app/pipeline.py`**: Connects the retriever and generator into a single callable function: `answer_question(question: str) -> str`.
10. **`app/main.py`**: Terminal-based chat interface that runs an interactive Q&A loop until the user types `exit`.

---

## Prerequisites

Before running the project, ensure the following are installed and running:

1. **Python 3.11** or newer
2. **Poetry** package manager
3. **Ollama** installed and running on your local machine (`http://localhost:11434`)

---

## Installation & Environment Setup

1. Clone or open the repository folder:
   ```powershell
   cd 16_SR_PHENG_MENGHEAK
   ```

2. Install Python dependencies using Poetry:
   ```powershell
   poetry install
   ```

3. Ensure Ollama is running and pull the required models:
   ```powershell
   ollama pull llama3.2:3b
   ollama pull nomic-embed-text
   ```

4. Verify installed models:
   ```powershell
   ollama list
   ```

---

## Configuration

All application hyperparameters are defined in `app/config.py`:

| Parameter | Value | Description |
| :--- | :--- | :--- |
| `EMBED_MODEL` | `"nomic-embed-text"` | Local embedding model used for documents and queries |
| `LLM_MODEL` | `"llama3.2:3b"` | Local language model used for grounded answer generation |
| `DATA_DIR` | `"data"` | Folder containing source documents |
| `CHROMA_DB_DIR` | `"chroma_db"` | Directory for ChromaDB persistent database files |
| `COLLECTION_NAME` | `"documents"` | Name of the ChromaDB collection |
| `CHUNK_SIZE` | `500` | Chunk size in characters |
| `CHUNK_OVERLAP` | `100` | Overlap between consecutive chunks in characters |
| `TOP_K` | `3` | Number of relevant chunks retrieved per query |

---

## Chunking Strategy & Rationale

### Strategy Used
**Fixed-size character chunking with sliding-window overlap** (`chunk_size=500`, `overlap=100`).

### Why This Strategy Was Chosen
1. **Context Predictability:** Breaking documents into 500-character segments ensures consistent vector representation sizes that fit comfortably within the embedding window of `nomic-embed-text`.
2. **Boundary Information Preservation:** A 100-character overlap (20% of chunk size) ensures that sentences, code snippets, or key concepts that lie on chunk boundaries are not abruptly split or lost during similarity search.
3. **Simplicity and Reliability:** It operates cleanly on plain text and technical documentation without introducing heavy parsing dependencies or risking parser failures.

---

## Building the ChromaDB Vector Index

Because `chroma_db/` is excluded from version control via `.gitignore`, the vector index must be built before starting the chat application.

Run the indexing script:
```powershell
poetry run python -m app.vector_store
```

Expected output:
```text
Indexed 20 chunks from 'data/' into Chroma at 'chroma_db/'
```

---

## Standalone Vector Store Verification

To test that ChromaDB and the embedding model are working properly without running the LLM generation step:

```powershell
poetry run python -m app.demo_vector_check
```

Enter a test question (e.g. `What is a REST API?`) to see the top 3 retrieved chunks, their sources, and chunk indices.

---

## Running the Terminal Chat Application

Launch the interactive chat interface:

```powershell
poetry run python -m app.main
```

Type any question grounded in the source documents. Type `exit` to terminate the session.

Example session:
```text
RAG Chatbot
Type 'exit' to quit.

You: What HTTP method is used to create a new resource?

Assistant: To create a new resource, the HTTP method POST is commonly used.

You: exit
Goodbye!
```

---

## RAG Workflow Overview

```text
Offline Pipeline (Setup):
  Documents (data/) 
    → Ingestion (load_documents) 
    → Chunking (chunk_text: 500 chars, 100 overlap) 
    → Embedding (embed_texts: nomic-embed-text) 
    → Storage (ChromaDB persistent collection)

Online Pipeline (Query Time):
  User Question 
    → Query Embedding (embed_query) 
    → Similarity Search (top_k=3 in ChromaDB) 
    → Prompt Construction (Context + Question + Grounded Instructions) 
    → LLM Generation (llama3.2:3b) 
    → Grounded Answer
```

---

## Submission Deliverables

1. **Code Files:** Located in `app/` (`config.py`, `ingestion.py`, `chunking.py`, `embeddings.py`, `vector_store.py`, `demo_vector_check.py`, `retriever.py`, `generator.py`, `pipeline.py`, `main.py`).
2. **Documentation (`README.md`):** Complete setup, architecture, and running instructions.
3. **Step 7 Test Log (`test_log.md`):** Full record of 5 real terminal evaluation tests (4 in-document, 1 out-of-document) with retrieved chunks and generated answers. See [test_log.md](test_log.md).
4. **Step 8 Reflection (`reflection.md`):** 150–300 word reflection covering what worked well, difficulties encountered, and a proposal for Advanced RAG improvements (Cross-Encoder Re-ranking). See [reflection.md](reflection.md).
