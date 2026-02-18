import os
from datetime import datetime

def run_stub():
    return (
        "STUB: Pinecone not configured yet "
        "(no PINECONE_API_KEY / index). "
        "This run proves module setup + artifact logging."
    )

def main():
    timestamp = datetime.now().isoformat(timespec="seconds")

    api_key = os.getenv("PINECONE_API_KEY")
    index = os.getenv("PINECONE_INDEX")
    env = os.getenv("PINECONE_ENV")

    query = "What did we build so far in Phase 2 (16-21)?"

    # If Pinecone credentials not set → run stub
    if not api_key or not index:
        mode = "stub"
        result = run_stub()
        index_name = "-"
        namespace = "-"
    else:
        # Placeholder for real Pinecone logic (to implement later)
        mode = "configured"
        result = "Real Pinecone query logic will be implemented later."
        index_name = index
        namespace = "default"

    output_text = f"""PHASE 2.22 - Pinecone Cloud Query
Date: {timestamp}
Command: python phase2_llm_nlp\\22_pinecone_cloud_query\\main.py
Mode: {mode}
Index: {index_name}
Namespace: {namespace}

Query:
{query}

Result:
{result}

Notes:
- To run real Pinecone query later, set environment variables:
  PINECONE_API_KEY
  PINECONE_INDEX
  PINECONE_ENV
"""

    # Write artifact
    with open(
        "phase2_llm_nlp/22_pinecone_cloud_query/output.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(output_text)

    print(output_text)


if __name__ == "__main__":
    main()
