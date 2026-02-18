from datetime import datetime

def llama_local_stub(prompt: str) -> str:
    """
    Local stub that mimics an LLM response without requiring a real model.
    This keeps the pipeline runnable on any machine.
    """
    rules = [
        ("hello", "Hello! I’m a local LLaMA stub. No model loaded, but the pipeline works."),
        ("who are you", "I’m a local LLaMA stub used for testing the LLM workflow offline."),
        ("summarize", "Stub summary: This is a placeholder response demonstrating offline LLM flow."),
    ]

    p = prompt.strip().lower()
    for key, resp in rules:
        if key in p:
            return resp

    return (
        "Stub response:\n"
        f"- Received prompt length: {len(prompt)}\n"
        "- No local model configured yet.\n"
        "- Next step: connect a real local LLM (Ollama / llama.cpp) when ready."
    )

def main():
    prompt = "Summarize what we did in Phase 2.17 and what Phase 2.18 is."
    out = llama_local_stub(prompt)

    text = []
    text.append("PHASE 2.18 — LLaMA Local Stub")
    text.append(f"Date: {datetime.now().isoformat(timespec='seconds')}")
    text.append("Command: python phase2_llm_nlp\\18_llama_local_stub\\main.py")
    text.append("")
    text.append("Prompt:")
    text.append(prompt)
    text.append("")
    text.append("Output:")
    text.append(out)

    print("\n".join(text))

    # Save artifact
    with open("phase2_llm_nlp/18_llama_local_stub/output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(text) + "\n")

if __name__ == "__main__":
    main()
