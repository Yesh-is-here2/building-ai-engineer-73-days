print("Mini CLI chatbot (placeholder). Type exit to stop.")
while True:
    msg = input("you> ").strip()
    if msg.lower() in ("exit","quit"):
        print("bot> bye")
        break
    if "help" in msg.lower():
        print("bot> Try: what is overfitting?")
    else:
        print("bot> Placeholder bot. Later I will connect to an LLM.")
