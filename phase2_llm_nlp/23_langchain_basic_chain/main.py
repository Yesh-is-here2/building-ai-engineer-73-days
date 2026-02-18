# phase2_llm_nlp/23_langchain_basic_chain/main.py

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path


MODULE = "PHASE 2.23 - LangChain Basic Chain"
OUTFILE = Path(__file__).with_name("output.txt")


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def write_output(text: str) -> None:
    OUTFILE.write_text(text, encoding="utf-8")


def try_langchain_chain(prompt: str) -> tuple[str, str]:
    """
    Returns: (mode, output)
    mode: "real" if it actually executed a LangChain chain,
          "stub" if it fell back.
    """
    # If user has OpenAI key AND langchain installed, attempt a real LCEL chain.
    # Otherwise, stub but still logs proof.
    openai_key = os.getenv("OPENAI_API_KEY", "").strip()

    try:
        # Import inside try so the script still runs even if langchain isn't installed.
        # Newer LangChain splits: langchain-core + langchain-openai
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.output_parsers import StrOutputParser

        if not openai_key:
            raise RuntimeError("OPENAI_API_KEY not set (running stub mode).")

        # Prefer langchain-openai if available
        try:
            from langchain_openai import ChatOpenAI
        except Exception as e:
            raise RuntimeError(
                "langchain_openai not installed. Install with: pip install langchain-openai"
            ) from e

        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

        prompt_tmpl = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a concise AI assistant."),
                ("user", "{question}"),
            ]
        )

        chain = prompt_tmpl | llm | StrOutputParser()
        output = chain.invoke({"question": prompt})
        return "real", output

    except Exception as e:
        # Stub fallback (always works)
        stub = (
            "STUB: LangChain chain not executed (missing key/deps). "
            "This run still proves module wiring + artifact logging.\n"
            f"Reason: {type(e).__name__}: {e}"
        )
        return "stub", stub


def main() -> None:
    prompt = "Explain what a LangChain 'chain' is in one paragraph, and give one simple example use-case."

    mode, result = try_langchain_chain(prompt)

    content = (
        f"{MODULE}\n"
        f"Date: {now_iso()}\n"
        f"Command: python phase2_llm_nlp\\23_langchain_basic_chain\\main.py\n"
        f"Mode: {mode}\n\n"
        f"Input:\n{prompt}\n\n"
        f"Output:\n{result}\n\n"
        "Notes:\n"
        "- If you want REAL mode, set OPENAI_API_KEY and install:\n"
        "  pip install langchain langchain-core langchain-openai\n"
    )

    print(content)
    write_output(content)


if __name__ == "__main__":
    main()
