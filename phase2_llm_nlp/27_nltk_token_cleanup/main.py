import os
import re
from datetime import datetime

import nltk


PHASE = "PHASE 2.27 - NLTK Token Cleanup"
HERE = os.path.dirname(__file__)
OUTPUT_PATH = os.path.join(HERE, "output.txt")


def ensure_nltk():
    # Only needed first time; safe to call repeatedly
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)


def clean_tokens(text: str):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    raw_tokens = word_tokenize(text)

    # Lowercase + keep only alphabetic tokens
    tokens = [t.lower() for t in raw_tokens]
    tokens = [t for t in tokens if re.fullmatch(r"[a-z]+", t)]

    stops = set(stopwords.words("english"))
    filtered = [t for t in tokens if t not in stops]

    return raw_tokens, tokens, filtered


def main():
    ensure_nltk()

    timestamp = datetime.now().isoformat(timespec="seconds")
    command = r"python phase2_llm_nlp\27_nltk_token_cleanup\main.py"

    text = (
        "RAG pipelines use embeddings + vector search (FAISS/Chroma) to retrieve context, "
        "then an LLM generates answers. Clean tokens help indexing and analytics!"
    )

    raw_tokens, alpha_lower_tokens, filtered = clean_tokens(text)

    log = f"""{PHASE}
Date: {timestamp}
Command: {command}

Input text:
{text}

Raw tokens (NLTK word_tokenize):
{raw_tokens}

Lowercased alphabetic tokens:
{alpha_lower_tokens}

After stopword removal:
{filtered}

Notes:
- We keep only alphabetic tokens for a clean vocabulary.
- Stopword removal reduces noise for simple NLP analytics.
"""

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(log)

    print(log)


if __name__ == "__main__":
    main()
