from datetime import datetime
import random

def main():
    name = "Yesh"
    today = datetime.now().date()

    emojis = ["🙂", "🚀", "🤖", "🔥"]

    print("Name:", name)
    print("Date:", today)
    print("Random emoji:", random.choice(emojis))


if __name__ == "__main__":
    main()
