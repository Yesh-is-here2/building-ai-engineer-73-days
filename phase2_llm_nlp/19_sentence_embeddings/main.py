from datetime import datetime
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def main():
    phase = "PHASE 2.19 — Sentence Embeddings"
    timestamp = datetime.now().isoformat(timespec="seconds")
    cmd = r"python phase2_llm_nlp\19_sentence_embeddings\main.py"

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    sentences = [
        "I love machine learning.",
        "Artificial intelligence is transforming industries.",
        "Pizza tastes great on weekends.",
        "Deep learning uses neural networks."
    ]

    model = SentenceTransformer(model_name)
    emb = model.encode(sentences, normalize_embeddings=False)

    # cosine similarity matrix
    sims = np.zeros((len(sentences), len(sentences)), dtype=float)
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            sims[i, j] = cosine_sim(emb[i], emb[j])

    # print to terminal
    print(phase)
    print(f"Date: {timestamp}")
    print(f"Command: {cmd}")
    print(f"Model: {model_name}")
    print(f"Embedding shape: {emb.shape}")
    print("Cosine similarity matrix:")
    print(np.round(sims, 4))

    # write artifact
    out_path = Path("phase2_llm_nlp/19_sentence_embeddings/output.txt")
    lines = []
    lines.append(f"{phase}")
    lines.append(f"Date: {timestamp}")
    lines.append(f"Command: {cmd}")
    lines.append(f"Model: {model_name}")
    lines.append("Sentences:")
    for s in sentences:
        lines.append(f"- {s}")
    lines.append(f"Embedding shape: {emb.shape}")
    lines.append("Cosine similarity matrix:")
    lines.append(str(np.round(sims, 4)))
    lines.append("Notes: Similar sentences should have higher similarity values.")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
