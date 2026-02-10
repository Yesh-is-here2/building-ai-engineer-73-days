import os
api_key = os.getenv("PINECONE_API_KEY")
index = os.getenv("PINECONE_INDEX")

if not api_key or not index:
    print("Pinecone safe stub.")
    print("Set: PINECONE_API_KEY and PINECONE_INDEX to run real calls.")
else:
    print("Pinecone env detected. Add real client calls here.")
