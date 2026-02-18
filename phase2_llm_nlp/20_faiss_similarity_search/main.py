from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from datetime import datetime

sentences = [
    "I love machine learning.",
    "Artificial intelligence is transforming industries.",
    "Pizza tastes great on weekends.",
    "Deep learning uses neural networks."
]

model_name = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(model_name)

embeddings = model.encode(sentences)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

query = "Neural networks and AI"
query_embedding = model.encode([query])

k = 2
distances, indices = index.search(np.array(query_embedding), k)

now = datetime.now().isoformat(timespec="seconds")

output_text = f"""PHASE 2.20 — FAISS Similarity Search
Date: {now}
Model: {model_name}

Query:
{query}

Top {k} Results:
"""

for rank, idx in enumerate(indices[0]):
    output_text += f"{rank+1}. {sentences[idx]} (distance={distances[0][rank]:.4f})\n"

with open("phase2_llm_nlp/20_faiss_similarity_search/output.txt", "w", encoding="utf-8") as f:
    f.write(output_text)

print(output_text)
