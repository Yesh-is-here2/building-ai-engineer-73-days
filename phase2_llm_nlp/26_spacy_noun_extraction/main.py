import os
from datetime import datetime
import spacy


PHASE = "PHASE 2.26 - spaCy Noun Extraction"
HERE = os.path.dirname(__file__)
OUTPUT_PATH = os.path.join(HERE, "output.txt")


def extract_nouns_and_chunks(text: str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    nouns = []
    for token in doc:
        if token.pos_ in ("NOUN", "PROPN"):
            nouns.append(token.text)

    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    return nouns, noun_chunks


def main():
    timestamp = datetime.now().isoformat(timespec="seconds")
    command = r"python phase2_llm_nlp\26_spacy_noun_extraction\main.py"

    text = (
        "LangChain and LangGraph help developers build LLM workflows. "
        "We used sentence embeddings with MiniLM, FAISS for similarity search, "
        "and vector databases like ChromaDB and Pinecone."
    )

    nouns, noun_chunks = extract_nouns_and_chunks(text)

    log = f"""{PHASE}
Date: {timestamp}
Command: {command}
Model: en_core_web_sm

Input text:
{text}

Extracted nouns / proper nouns:
- """ + "\n- ".join(nouns) + """

Noun chunks:
- """ + "\n- ".join(noun_chunks) + """
"""

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(log)

    print(log)


if __name__ == "__main__":
    main()
