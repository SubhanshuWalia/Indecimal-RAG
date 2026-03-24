import os, glob, requests, json
from dotenv import load_dotenv
import os

load_dotenv() 
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not os.getenv("OPENROUTER_API_KEY"):
    raise RuntimeError("OPENROUTER_API_KEY is missing; set env var or load .env file")

EMBED_MODEL = "nvidia/llama-nemotron-embed-vl-1b-v2:free"

def chunk_text(text, chunk_size=250, overlap=50):
    words = text.split()
    step = chunk_size - overlap
    out = []
    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i+chunk_size])
        if chunk:
            out.append(chunk)
    return out

def load_and_chunk_docs(folder="data/*.md"):
    all_chunks = []
    for path in glob.glob(folder):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        chunks = chunk_text(text, chunk_size=250, overlap=50)
        for idx, c in enumerate(chunks):
            all_chunks.append({"doc": path, "chunk_id": idx, "text": c})
    return all_chunks

def embed_texts(texts):
    url = "https://openrouter.ai/api/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {"model": EMBED_MODEL, "input": texts}
    r = requests.post(url, headers=headers, json=data, timeout=90)
    r.raise_for_status()
    out = r.json()
    return [item["embedding"] for item in out["data"]]

def main():
    chunks = load_and_chunk_docs("data/*.md")
    texts = [c["text"] for c in chunks]
    embeddings = embed_texts(texts)
    with open("data/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    with open("data/embeddings.npy", "wb") as f:
        import numpy as np
        np.save(f, np.array(embeddings, dtype="float32"))
    print(f"chunks={len(chunks)}, embeddings saved")

if __name__ == "__main__":
    main()