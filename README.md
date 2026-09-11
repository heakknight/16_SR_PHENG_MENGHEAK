# Baseline RAG Document Chat

A simple local Retrieval-Augmented Generation (RAG) application built with
Python, Ollama, and ChromaDB.

The application reads local documents, splits them into chunks, creates
embeddings, stores them in ChromaDB, retrieves relevant chunks for a question,
and uses a local LLM to generate an answer based on the retrieved information.

## Technology Stack

- Python 3.11
- Poetry
- Ollama
- ChromaDB
- `nomic-embed-text` - embedding model
- `llama3.2:3b` - generation model

## Project Structure

```text
16_SR_PHENG_MENGHEAK/
├── app/
│   ├── config.py
│   ├── ingestion.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── demo_vector_check.py
│   ├── retriever.py
│   ├── generator.py
│   ├── pipeline.py
│   └── main.py
├── data/
│   ├── python_development_guide.txt
│   ├── rag_application.txt
│   └── rest_api_guide.txt
├── chroma_db/
├── test_log.md
├── reflection.md
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Prerequisites

Before running the application, install:

- Python 3.11 or newer
- Poetry
- Ollama

Ollama must be running on the local machine.

## Installation

Install the project dependencies:

```powershell
poetry install
```

Pull the required Ollama models:

```powershell
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

Check that the models are installed:

```powershell
ollama list
```

## Configuration

The main settings are stored in `app/config.py`.

```python
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2:3b"

DATA_DIR = "data"
CHROMA_DB_DIR = "chroma_db"
COLLECTION_NAME = "documents"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K = 3
```

## Source Documents

The project uses three text documents:

- `python_development_guide.txt`
- `rag_application.txt`
- `rest_api_guide.txt`

They are stored in the `data/` directory.

## Chunking Strategy

I used fixed-size character chunking with overlap.

- Chunk size: 500 characters
- Overlap: 100 characters

I chose this method because it is simple and easy to understand for a
baseline RAG application. The overlap also helps keep information that may
be close to the boundary between two chunks.

## Build the Vector Store

Before running the chat application, build the ChromaDB index:

```powershell
poetry run python -m app.vector_store
```

This loads the documents, creates chunks, generates embeddings, and stores
the chunks and embeddings in ChromaDB.

## Check the Vector Store

The vector store can be tested separately with:

```powershell
poetry run python -m app.demo_vector_check
```

Enter a question in the terminal to see the top 3 retrieved chunks.

## Run the Chat Application

Start the RAG chatbot with:

```powershell
poetry run python -m app.main
```

Example:

```text
RAG Chatbot
Type 'exit' to quit.

You: What HTTP method is used to create a new resource?

Assistant: To create a new resource, the HTTP method POST is commonly used.

You: exit
```

Type `exit` to quit.

## RAG Workflow

```text
Documents
    ↓
Ingestion
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Retrieval
    ↓
Prompt
    ↓
Local LLM
    ↓
Answer
```

## Test Results

The application was tested with 5 questions:

- 4 questions that could be answered from the documents
- 1 question that was not covered by the documents

The detailed questions, retrieved chunks, and generated answers are recorded
in `test_log.md`.

## Reflection

The project reflection is recorded in `reflection.md`.
