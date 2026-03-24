# BEAM 🏗️
### Precision RAG Chatbot for Indecimal Construction

**BEAM** is a mini-RAG (Retrieval-Augmented Generation) pipeline designed to extract information from technical construction documents and provide grounded, AI-powered answers via a Streamlit interface.

---

## 🛠️ Tech Stack

- **LLM & Embeddings:** [OpenRouter API](https://openrouter.ai/)
  - **Embedding Model:** `nvidia/llama-nemotron-embed-vl-1b-v2:free`
  - **Generation Model:** OpenRouter Free LLMs
- **Vector Database:** [FAISS](https://github.com/facebookresearch/faiss) (Facebook AI Similarity Search)
- **Web Framework:** [Streamlit](https://streamlit.io/)
- **Core Libraries:** `numpy`, `python-dotenv`, `tiktoken`, `requests`

---

## 📐 Architecture

The system is built on five core pillars:

1.  **Document Processing:** Loads, cleans, and chunks `.md` documents into manageable segments.
2.  **Vector Search:** Generates high-dimensional embeddings and manages the FAISS index for lightning-fast similarity lookups.
3.  **Query Processing:** Converts user questions into vectors to retrieve the Top-K most relevant context chunks.
4.  **Grounding Evaluation:** A custom scoring system that assesses how well the LLM's answer is supported by the retrieved data to prevent hallucinations.
5.  **BEAM Interface:** A user-friendly chat environment with real-time transparency.

---

## 📊 Evaluation & Grounding

To ensure reliability on the construction site, every answer is assigned a **Grounding Score**:

| Metric | Score | Meaning |
| :--- | :--- | :--- |
| **High Grounding** | 0.7 - 1.0 | Answer is well-supported by retrieved chunks. |
| **Medium Grounding** | 0.4 - 0.7 | Answer is relevant but may contain general knowledge. |
| **Low Grounding** | < 0.4 | **High Hallucination Risk.** Proceed with caution. |

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the necessary Python packages:


## Building: Run the following commands.
1. `python embedding.py` # Generates chunks and embeddings
2. `python vector_search.py` # Builds FAISS index

## Usage: Running web interface
1. `streamlit run app.py`

## File structure:
```text
├── app.py                 # Streamlit web interface
├── embedding.py           # Document processing and embedding
├── vector_search.py       # FAISS index management
├── search_answer.py       # Query embedding and LLM generation
├── evaluation.py          # Grounding evaluation
├── prequisite.txt         # Python dependencies
├── readme.md              # This documentation
├── result.json            # Example evaluation output
├── data/
│   ├── chunks.json        # Processed document chunks
│   ├── embeddings.npy     # Embedding vectors
│   ├── faiss.index        # FAISS search index
│   ├── doc1.md            # Document 1
│   ├── doc2.md            # Document 2
│   └── doc3.md            # Document 3
```


Install prerequisites `pip install -r prerequisite.txt`

## Building: Run the following commands.
1. `python embedding.py` # Generates chunks and embeddings
2. `python vector_search.py` # Builds FAISS index

## Usage: Running web interface
1. `streamlit run app.py`

## Features
1. **BEAM Interface**: The web interface is named **BEAM**, providing a streamlined environment for construction-related queries.
2. **Grounding Score**: When a user submits a query, the bot returns an answer accompanied by an evaluation score expressed as **% grounding** to indicate factual reliability.
3. **Source Transparency**: Includes a **dropdown menu** that reveals the specific **top-k retrieved chunks** used to generate the response.
4. **Dynamic Retrieval**: The **side panel** features a **slider** allowing users to adjust the number of retrieved chunks (top-k) as per their convenience.
5. **Session Management**: **Chat history** is persistently stored and displayed in the main chat window; it can be reset at any time using the **Clear Chat** button in the side panel.
