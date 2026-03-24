Building a Mini RAG! "BEAM"
This is a mini RAG pipeline to extract info from given documents and use as a mini chatbot.

Architecture: The sytem consists of the following componenets
1. Document processing and embedding: Loads and chunks the documents and generates embeddings.
2. Vector Search: Builds and manages FAISS index for similarity search.
3. Query processing: Embeds Query and generates LLM response with the retreived top-k chunks. 
4. Evaluation: Assess answer grounding to check relevance and hallucinations. 
5. Web interface: Streamlit based chat interface "BEAM". 

Tech Stack:
1. Embedding Model Used: OpenRouter API
                      nvidia/llama-nemotron-embed-vl-1b-v2:free

2. Vector Search Used: FAISS (Facebook AI Similarity Search)

3. LLM USed: OpenRouter API - Free LLMs
4. Retrieve context and hallucination evaluation: Grounding Score
    Metric              Score           Meaning
    High Grounding      1.0 - 0.7       Answer well supported by chunks
    Medium Grounding    0.4 - 0.7       Answer relevant to chunks
    Low Grounding       < 0.4           High Hallucination risk

Libraries used:
1. Streamlit: Web interface
2. faiss-cpu: Vector similarity search
3. numpy: Numerical computation
4. python-dotenv: OpenAI compatibilit for OpenRouter
5. tiktoken: Token counting for evaluation

Installation:
1. Clone the repository.
2. Install dependencies: pip -install -r prerequisite.txt

Building: Run the following commands.
1. python embedding.py # Generates chunks and embeddings
2. python vector_search.py #  Builds FAISS index

Usage: Running web interface
1. streamlit run app.py  

FIle structure:

├── app.py                 # Streamlit web interface
├── embedding.py           # Document processing and embedding
├── vector_search.py       # FAISS index management
├── search_answer.py       # Query embedding and LLM generation
├── evaluation.py          # Grounding evaluation
├── prequisite.txt         # Python dependencies
├── readme.md             # This documentation
├── result.json           # Example evaluation output
├── data/
│   ├── chunks.json       # Processed document chunks
│   ├── embeddings.npy    # Embedding vectors
│   ├── faiss.index       # FAISS search index
│   ├── doc1.md           # Document 1
│   ├── doc2.md           # Document 2
│   └── doc3.md           # Document 3


1. The web interface is named BEAM.
2. When user give a query the bot returns the answer with the evaluation score as %grounding.
3. Theres a dropdown which shows the top-k retrived chunks fro the answer.
4. There a sidepain which contains a slider to change the top-k returned chunks as per the users convenience.
5. Chat history is stored and displayed in the main chat always whch can be cleared by clicking on the clear chat button in the side pain.
