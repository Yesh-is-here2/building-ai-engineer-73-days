from datetime import datetime
import json
import chromadb


def write_output(text: str, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out_path = "phase2_llm_nlp/21_chromadb_store_retrieve/output.txt"
    now = datetime.now().isoformat(timespec="seconds")

    client = chromadb.Client()
    col = client.get_or_create_collection(name="demo")

    # store
    col.add(
        ids=["a", "b"],
        documents=["cats", "dogs"],
    )

    # retrieve
    result = col.query(
        query_texts=["cats"],
        n_results=2,
        include=["documents", "distances", "metadatas"],
    )

    # pretty log
    log = []
    log.append("PHASE 2.21 — ChromaDB Store + Retrieve")
    log.append(f"Date: {now}")
    log.append("Command: python phase2_llm_nlp\\21_chromadb_store_retrieve\\main.py")
    log.append("")
    log.append("Query: cats")
    log.append("")
    log.append("Raw result:")
    log.append(json.dumps(result, indent=2))
    log.append("")

    text = "\n".join(log)
    print(text)
    write_output(text, out_path)


if __name__ == "__main__":
    main()
