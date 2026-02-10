def transform(text: str) -> str:
    return text.strip().lower().replace(" ", "-")

if __name__ == "__main__":
    s = " Building AI Engineer "
    print("in :", s)
    print("out:", transform(s))
