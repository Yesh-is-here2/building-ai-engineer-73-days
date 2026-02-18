import os
from datetime import datetime

PHASE = "PHASE 2.30 - LLM CLI Chatbot (Offline Stub)"
HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "output.txt")


def stub_llm(user_msg: str) -> str:
    """
    Offline "LLM" behavior:
    - echoes intent
    - gives a structured response
    This is just to prove CLI chat loop + logging artifact.
    """
    msg = user_msg.strip()
    if not msg:
        return "Please type something."
    if msg.lower() in {"exit", "quit"}:
        return "__EXIT__"
    if "embedding" in msg.lower():
        return "Embeddings map text to vectors so we can compare meaning using distances (e.g., cosine)."
    if "rag" in msg.lower():
        return "RAG = retrieve relevant docs (vector search) then generate an answer grounded in them."
    return f"Stub reply: I received your message and would answer it here. You said: '{msg}'"


def main():
    ts = datetime.now().isoformat(timespec="seconds")
    cmd = r"python phase2_llm_nlp\30_llm_cli_chatbot\main.py"

    # We run a short scripted chat so you always get a proof artifact
    scripted = [
        "Hi, what did we learn in Phase 2 so far?",
        "Explain embeddings in one line.",
        "What is RAG?",
        "exit",
    ]

    lines = []
    lines.append(PHASE)
    lines.append(f"Date: {ts}")
    lines.append(f"Command: {cmd}")
    lines.append("")
    lines.append("Scripted chat transcript:")
    lines.append("")

    for user_msg in scripted:
        lines.append(f"You: {user_msg}")
        reply = stub_llm(user_msg)
        if reply == "__EXIT__":
            lines.append("Bot: Exiting. (stub)")
            break
        lines.append(f"Bot: {reply}")
        lines.append("-" * 60)

    text = "\n".join(lines) + "\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)

    print(text)
    print(f"[saved] {OUT}")


if __name__ == "__main__":
    main()
