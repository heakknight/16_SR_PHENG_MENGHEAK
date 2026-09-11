# Step 7: RAG Application Test Log

This test log documents the evaluation of the Baseline RAG Document Chat application against 5 questions (4 in-document questions testing information retrieval and grounded answering across all source documents, and 1 out-of-document question testing hallucination rejection).

All tests were executed on the live terminal application using `nomic-embed-text` embeddings, ChromaDB vector store, and `llama3.2:3b` generation.

---

## Test 1: HTTP Methods and Status Codes (In-Document)

* **Source Document:** `rest_api_guide.txt`
* **Question:**
  > What HTTP method is used to create a new resource, and which status code indicates success?

* **Retrieved Chunks:**
  1. **Source:** `rest_api_guide.txt` | **Chunk Index:** 1 | **Distance:** 0.3745
     ```text
     request body.

     **Step 2: Use HTTP Methods**

     1. GET is commonly used to retrieve data.
     2. POST is commonly used to create a new resource.
     3. PUT is commonly used to replace an existing resource.
     4. PATCH is commonly used to partially update a resource.
     5. DELETE is commonly used to remove a resource.

     **Step 3: Understand Status Codes**

     Common HTTP status codes include:

     * 200 means the request was successful.
     * 201 means a resource was successfully created.
     * 400 means the request contains in
     ```
  2. **Source:** `rag_application.txt` | **Chunk Index:** 5 | **Distance:** 0.5658
     ```text
     he question is about HTTP status codes, the system should retrieve chunks from a document that discusses REST APIs and status codes.

     **Step 7: Generate an Answer**

     The retrieved chunks are provided to a language model together with the user's question.

     A grounded system prompt can instruct the model to answer using only the retrieved context. If the context does not contain the answer, the model should say that there is not enough information instead of inventing an answer.

     **Step 8: Test th
     ```
  3. **Source:** `rest_api_guide.txt` | **Chunk Index:** 2 | **Distance:** 0.5980
     ```text
     was successful.
     * 201 means a resource was successfully created.
     * 400 means the request contains invalid client data.
     * 401 means authentication is required or invalid.
     * 403 means the client is not allowed to perform the requested action.
     * 404 means the requested resource was not found.
     * 500 indicates a server-side error.

     **Step 4: Work With JSON**

     JSON is commonly used to exchange structured data between a client and an API.

     For example, a user response may contain fields such as:

     * id
     ```

* **Final Generated Answer:**
  > To create a new resource, the HTTP method POST is commonly used.
  > 
  > A status code of 201 means a resource was successfully created.
  > 
  > Source files: [2] rag_application.txt and [3] rest_api_guide.txt

* **Evaluation:**
  - **Result:** Pass
  - **Notes:** The model accurately identified `POST` and `201` directly from `rest_api_guide.txt` and cited the source documents.

---

## Test 2: Chunk Overlap Purpose (In-Document)

* **Source Document:** `rag_application.txt`
* **Question:**
  > Why is overlap used when splitting documents into chunks?

* **Retrieved Chunks:**
  1. **Source:** `rag_application.txt` | **Chunk Index:** 2 | **Distance:** 0.5921
     ```text
     smaller chunks before they are embedded.

     A chunking strategy can use a fixed size and an overlap. For example, a project may use a chunk size of 500 characters and an overlap of 100 characters.

     Overlap helps preserve information when an important sentence is close to a chunk boundary.

     The goal of chunking is:

     large text → smaller meaningful pieces

     **Step 4: Create Embeddings**

     An embedding model converts each text chunk into a numerical vector.

     Texts with similar meanings should generally
     ```
  2. **Source:** `rag_application.txt` | **Chunk Index:** 1 | **Distance:** 0.7696
     ```text
     it easier to create useful questions later.

     **Step 2: Ingest Documents**

     The ingestion stage loads source files and converts them into text.

     For text files, Python can read the file contents directly. For PDF files, a PDF reader can extract text from each page.

     The goal of ingestion is:

     source files → clean text

     **Step 3: Split Documents Into Chunks**

     Large documents should be divided into smaller chunks before they are embedded.

     A chunking strategy can use a fixed size and an overlap. F
     ```
  3. **Source:** `rag_application.txt` | **Chunk Index:** 7 | **Distance:** 0.7770
     ```text
     t-of-document question, the system should avoid pretending that the documents contain the answer.

     **Troubleshooting Tips:**

     * If retrieval is poor, inspect the chunks first.
     * Check that document embeddings and query embeddings use the same model.
     * Check the chunk size and overlap.
     * Print the retrieved chunks before sending them to the language model.
     * Make sure the vector database contains the latest version of the documents.

     **Important Concept:**

     RAG does not simply make a language mod
     ```

* **Final Generated Answer:**
  > According to [1] rag_application.txt, overlap is used when splitting documents into chunks to preserve information when an important sentence is close to a chunk boundary.

* **Evaluation:**
  - **Result:** Pass
  - **Notes:** High-precision retrieval with the primary chunk ranking #1 (distance 0.5921). Grounded answer explicitly attributes the reasoning to `rag_application.txt`.

---

## Test 3: Python Context Managers (In-Document)

* **Source Document:** `python_development_guide.txt`
* **Question:**
  > Why should a developer use a with statement when reading a file in Python?

* **Retrieved Chunks:**
  1. **Source:** `python_development_guide.txt` | **Chunk Index:** 2 | **Distance:** 0.6698
     ```text
     Step 3: Read a Text File**

     Python can read a text file using the built-in `open()` function.

     1. Provide the file path.
     2. Open the file using read mode.
     3. Specify UTF-8 encoding when appropriate.
     4. Read the contents of the file.
     5. Use a `with` statement so the file is closed automatically.

     **Step 4: Use Lists and Dictionaries**

     A list stores an ordered collection of values. A dictionary stores information using key-value pairs.

     For example, a list can contain several document chunks, whi
     ```
  2. **Source:** `python_development_guide.txt` | **Chunk Index:** 1 | **Distance:** 0.8112
     ```text
     ual environment before installing dependencies.

     **Step 2: Work With Functions**

     Functions are reusable blocks of code that perform a specific task.

     1. Define a function using the `def` keyword.
     2. Add parameters when the function needs input.
     3. Use a return statement when the function needs to produce a value.
     4. Use type hints such as `text: str` and `-> int` to make expected types clear.

     **Step 3: Read a Text File**

     Python can read a text file using the built-in `open()` function.

     1. Pr
     ```
  3. **Source:** `python_development_guide.txt` | **Chunk Index:** 3 | **Distance:** 0.8573
     ```text
     res information using key-value pairs.

     For example, a list can contain several document chunks, while a dictionary can store metadata such as a source filename and chunk index.

     **Step 5: Handle Errors**

     Python uses `try` and `except` blocks to handle exceptions.

     1. Put code that may fail inside the `try` block.
     2. Handle the expected exception in the `except` block.
     3. Provide a useful response or fallback when possible.

     **Troubleshooting Tips:**

     * Check that the Python interpreter is corr
     ```

* **Final Generated Answer:**
  > According to [1] python_development_guide.txt, a developer should use a `with` statement when reading a file in Python because it automatically closes the file after reading its contents, thereby avoiding the need to explicitly close the file using a `close()` method or a try-finally block. This helps ensure that system resources are properly released and reduces the risk of file descriptor leaks.

* **Evaluation:**
  - **Result:** Pass
  - **Notes:** The retriever isolated the file operations section from `python_development_guide.txt`, and the model correctly answered that the file is closed automatically.

---

## Test 4: Storing Metadata in Vector Store (In-Document)

* **Source Document:** `rag_application.txt`
* **Question:**
  > What metadata can be stored alongside embeddings in a vector database?

* **Retrieved Chunks:**
  1. **Source:** `rag_application.txt` | **Chunk Index:** 3 | **Distance:** 0.4426
     ```text
     odel converts each text chunk into a numerical vector.

     Texts with similar meanings should generally have similar vectors. The same embedding model should be used when creating document embeddings and when embedding user questions.

     The goal is:

     text chunk → embedding vector

     **Step 5: Store the Index**

     A vector database stores the embedding together with the original chunk and useful metadata.

     Metadata can include:

     * source filename
     * chunk index
     * document type

     ChromaDB can be used as a l
     ```
  2. **Source:** `rag_application.txt` | **Chunk Index:** 4 | **Distance:** 0.4591
     ```text
     Metadata can include:

     * source filename
     * chunk index
     * document type

     ChromaDB can be used as a local vector database for a small RAG application.

     **Step 6: Retrieve Relevant Chunks**

     When a user asks a question, the application converts the question into an embedding.

     The vector database compares the question vector with stored vectors and returns the most similar chunks.

     For example, if the question is about HTTP status codes, the system should retrieve chunks from a document that discu
     ```
  3. **Source:** `rag_application.txt` | **Chunk Index:** 7 | **Distance:** 0.7169
     ```text
     t-of-document question, the system should avoid pretending that the documents contain the answer.

     **Troubleshooting Tips:**

     * If retrieval is poor, inspect the chunks first.
     * Check that document embeddings and query embeddings use the same model.
     * Check the chunk size and overlap.
     * Print the retrieved chunks before sending them to the language model.
     * Make sure the vector database contains the latest version of the documents.

     **Important Concept:**

     RAG does not simply make a language mod
     ```

* **Final Generated Answer:**
  > According to the context, metadata that can be stored alongside embeddings in a vector database are:
  > 
  > * source filename
  > * chunk index
  > * document type

* **Evaluation:**
  - **Result:** Pass
  - **Notes:** Top 2 retrieved chunks had very close semantic distance (< 0.46) and contained the exact bullet points from `rag_application.txt`. The model returned the exact list without hallucination.

---

## Test 5: Out-of-Document Question (Rejection Test)

* **Source Document:** None (Out of Scope)
* **Question:**
  > What is the capital city of France and what is its official currency?

* **Retrieved Chunks:**
  1. **Source:** `rag_application.txt` | **Chunk Index:** 4 | **Distance:** 1.2262
     ```text
     Metadata can include:

     * source filename
     * chunk index
     * document type

     ChromaDB can be used as a local vector database for a small RAG application.

     **Step 6: Retrieve Relevant Chunks**

     When a user asks a question, the application converts the question into an embedding.

     The vector database compares the question vector with stored vectors and returns the most similar chunks.

     For example, if the question is about HTTP status codes, the system should retrieve chunks from a document that discu
     ```
  2. **Source:** `rag_application.txt` | **Chunk Index:** 3 | **Distance:** 1.2383
     ```text
     odel converts each text chunk into a numerical vector.

     Texts with similar meanings should generally have similar vectors. The same embedding model should be used when creating document embeddings and when embedding user questions.

     The goal is:

     text chunk → embedding vector

     **Step 5: Store the Index**

     A vector database stores the embedding together with the original chunk and useful metadata.

     Metadata can include:

     * source filename
     * chunk index
     * document type

     ChromaDB can be used as a l
     ```
  3. **Source:** `python_development_guide.txt` | **Chunk Index:** 2 | **Distance:** 1.2430
     ```text
     Step 3: Read a Text File**

     Python can read a text file using the built-in `open()` function.

     1. Provide the file path.
     2. Open the file using read mode.
     3. Specify UTF-8 encoding when appropriate.
     4. Read the contents of the file.
     5. Use a `with` statement so the file is closed automatically.

     **Step 4: Use Lists and Dictionaries**

     A list stores an ordered collection of values. A dictionary stores information using key-value pairs.

     For example, a list can contain several document chunks, whi
     ```

* **Final Generated Answer:**
  > I don't have enough information in the documents to answer that. The context provides examples and general information about how a RAG application works with ChromaDB as a local vector database, but it does not provide specific details on how to retrieve answers to user questions like "What is the capital city of France and what is its official currency?"

* **Evaluation:**
  - **Result:** Pass
  - **Notes:** The distance metric for all retrieved chunks was high (> 1.22), reflecting minimal semantic similarity. Even though the underlying LLM knows world geography, the strict prompt instructions prevented it from answering from parametric memory, successfully replying that there is not enough information in the documents.

---

## Test Summary Table

| Test # | Topic | Document Category | Primary Retrieved Source | Semantic Distance | Grounded & Accurate? |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **1** | POST method & 201 status | In-Document | `rest_api_guide.txt` | `0.3745` | Yes |
| **2** | Purpose of chunk overlap | In-Document | `rag_application.txt` | `0.5921` | Yes |
| **3** | Python `with` statement | In-Document | `python_development_guide.txt` | `0.6698` | Yes |
| **4** | Metadata stored in vector DB | In-Document | `rag_application.txt` | `0.4426` | Yes |
| **5** | Capital & currency of France | Out-of-Document | None (distances > 1.22) | `1.2262` | Yes (Correctly declined) |
