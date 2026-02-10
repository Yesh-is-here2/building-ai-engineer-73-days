from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

text = "I am building AI skills step by step."
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

print("Loading:", model_name)
tok = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

batch = tok(text, return_tensors="pt")
print("token shapes:", {k: tuple(v.shape) for k,v in batch.items()})

with torch.no_grad():
    out = model(**batch)

pred = int(torch.argmax(out.logits, dim=1).item())
print("label:", model.config.id2label[pred])
