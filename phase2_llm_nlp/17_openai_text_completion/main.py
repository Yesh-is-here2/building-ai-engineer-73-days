import os
from openai import OpenAI

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("ERROR: OPENAI_API_KEY is not set in environment variables.")

    client = OpenAI(api_key=api_key)

    prompt = "Give me 3 bullet points on why version control matters for ML projects."

    resp = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    # Print only the final text
    print(resp.output_text)

if __name__ == "__main__":
    main()
