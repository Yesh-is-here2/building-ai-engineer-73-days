import spacy

text = "Building AI projects on GitHub improves my portfolio."
try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    print("spaCy model missing. Install:")
    print("python -m spacy download en_core_web_sm")
    raise

doc = nlp(text)
nouns = [t.text for t in doc if t.pos_ in ("NOUN","PROPN")]
print("nouns:", nouns)
