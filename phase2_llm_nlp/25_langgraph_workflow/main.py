import os
from datetime import datetime
from typing import TypedDict, Optional

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END


PHASE = "PHASE 2.25 - LangGraph Workflow"
HERE = os.path.dirname(__file__)
OUTPUT_PATH = os.path.join(HERE, "output.txt")


class State(TypedDict):
    question: str
    route: Optional[str]
    answer: Optional[str]


def router(state: State) -> State:
    """Decide which path to take based on the question."""
    q = state["question"].lower()
    if any(k in q for k in ["summarize", "summary", "bullet", "points"]):
        state["route"] = "summarize"
    else:
        state["route"] = "answer"
    return state


def llm_answer(state: State) -> State:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
    msg = f"Answer clearly in 4-6 lines:\n\nQuestion: {state['question']}"
    state["answer"] = llm.invoke(msg).content
    return state


def llm_summarize(state: State) -> State:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
    msg = f"Summarize in 5 bullet points:\n\nText: {state['question']}"
    state["answer"] = llm.invoke(msg).content
    return state


def choose_next(state: State) -> str:
    return "summarize" if state.get("route") == "summarize" else "answer"


def main():
    timestamp = datetime.now().isoformat(timespec="seconds")
    command = r"python phase2_llm_nlp\25_langgraph_workflow\main.py"

    question = "Summarize what we built in Phase 2 so far (16-25)."

    graph = StateGraph(State)

    graph.add_node("router", router)
    graph.add_node("answer", llm_answer)
    graph.add_node("summarize", llm_summarize)

    graph.set_entry_point("router")
    graph.add_conditional_edges("router", choose_next, {"answer": "answer", "summarize": "summarize"})
    graph.add_edge("answer", END)
    graph.add_edge("summarize", END)

    app = graph.compile()

    result = app.invoke({"question": question, "route": None, "answer": None})

    log = f"""{PHASE}
Date: {timestamp}
Command: {command}
Mode: real

Input:
{question}

Route chosen: {result.get("route")}

Output:
{result.get("answer")}
"""

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(log)

    print(log)


if __name__ == "__main__":
    main()
