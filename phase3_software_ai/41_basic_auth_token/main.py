TOKEN = "secret123"

def check(token: str) -> bool:
    return token == TOKEN

if __name__ == "__main__":
    t = "secret123"
    print("token ok?" , check(t))
