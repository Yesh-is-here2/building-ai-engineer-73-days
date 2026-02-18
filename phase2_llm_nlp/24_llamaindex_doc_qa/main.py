import os
from datetime import datetime

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI

PHASE = "PHASE 2.24 - LlamaIndex Document QA"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "output.txt")

timestamp = datetime.now().isoformat(timespec="seconds")

query = "What did we build in Phase 2 so far?"

mode = "real"

# Use local embeddings (no OpenAI embeddings cost)
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Use OpenAI for answer generation
Settings.llm = OpenAI(model="gpt-3.5-turbo")

# Create simple local document
doc_path = os.path.join(os.path.dirname(__file__), "doc.txt")
with open(doc_path, "w", encoding="utf-8") as f:
    f.write(
        "Phase 2 includes tokenization, OpenAI completions, "
        "LLaMA local stub, sentence embeddings, FAISS similarity search, "
        "ChromaDB store/retrieve, Pinecone cloud query, LangChain chain, "
        "and LlamaIndex document QA."
    )

documents = SimpleDirectoryReader(input_files=[doc_path]).load_data()

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query(query)

log = f"""{PHASE}
Date: {timestamp}
Command: python phase2_llm_nlp\\24_llamaindex_doc_qa\\main.py
Mode: {mode}

Query:
{query}

Output:
{response}
"""

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(log)

print(log)
