import os

prompt = "Write one sentence about building AI skills daily."
key = os.getenv("OPENAI_API_KEY")

print("Prompt:", prompt)

if not key:
    print("\nOPENAI_API_KEY not set -> safe stub mode.")
    print("When ready: set OPENAI_API_KEY and add the OpenAI SDK call here.")
else:
    print("\nOPENAI_API_KEY detected (not printing it).")
    print("Next step: wire official OpenAI SDK call.")
