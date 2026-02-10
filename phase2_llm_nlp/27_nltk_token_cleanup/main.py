import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

text = "This is a small sentence for tokenization and stopword removal."
tokens = word_tokenize(text.lower())
sw = set(stopwords.words("english"))
clean = [t for t in tokens if t.isalpha() and t not in sw]

print("tokens:", tokens)
print("clean:", clean)
