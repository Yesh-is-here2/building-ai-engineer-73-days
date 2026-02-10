import numpy as np
import faiss

np.random.seed(0)
vecs = np.random.randn(5, 8).astype("float32")
query = vecs[2:3]

index = faiss.IndexFlatL2(vecs.shape[1])
index.add(vecs)

D, I = index.search(query, k=3)
print("top indices:", I[0].tolist())
print("distances:", D[0].tolist())
