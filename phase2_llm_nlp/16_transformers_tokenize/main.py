import os
import json
from transformers import AutoTokenizer

BASE_DIR = os.path.dirname(__file__)
ARTIFACTS = os.path.join(BASE_DIR, "artifacts")
LOGS = os.path.join(ARTIFACTS, "logs")
OUT = os.path.join(ARTIFACTS, "outputs")

os.makedirs(LOGS, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

text = "Hello Yesh. Today we tokenize text using Transformers."

tokens = tokenizer.tokenize(text)
encoded = tokenizer(text)

report = {
    "model": model_name,
    "text": text,
    "tokens": tokens,
    "input_ids": encoded["input_ids"],
    "attention_mask": encoded["attention_mask"],
    "token_count": len(tokens),
}

with open(os.path.join(OUT, "tokenization_report.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2)

with open(os.path.join(LOGS, "run_log.txt"), "w", encoding="utf-8") as f:
    f.write(f"Model: {model_name}\n")
    f.write(f"Text: {text}\n\n")
    f.write(f"Tokens ({len(tokens)}):\n{tokens}\n\n")
    f.write(f"Input IDs:\n{encoded['input_ids']}\n")
    f.write(f"Attention Mask:\n{encoded['attention_mask']}\n")

print("Tokenization complete.")
print("Artifacts saved successfully.")
