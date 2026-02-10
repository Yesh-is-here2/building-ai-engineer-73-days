from sentence_transformers import SentenceTransformer

model_name = "all-MiniLM-L6-v2"
m = SentenceTransformer(model_name)

sents = ["cats are great", "I like machine learning", "pizza is tasty"]
emb = m.encode(sents)

print("model:", model_name)
print("embedding shape:", emb.shape)
print("first dims:", emb[0][:5])
