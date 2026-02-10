BANNED = {"bannedword1", "bannedword2", "bannedword"}

def allow(text: str) -> bool:
    words = {w.strip(".,!?").lower() for w in text.split()}
    return len(words & BANNED) == 0

tests = ["hello there", "this contains bannedword"]
for t in tests:
    print(t, "=>", "ALLOW" if allow(t) else "BLOCK")
