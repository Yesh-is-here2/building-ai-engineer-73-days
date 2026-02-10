import chromadb

client = chromadb.Client()
col = client.get_or_create_collection("demo")

col.add(
    ids=["a","b","c"],
    documents=["cats", "dogs", "machine learning"]
)

res = col.query(query_texts=["cats"], n_results=2)
print(res)
