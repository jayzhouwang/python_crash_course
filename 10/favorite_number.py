import json

filename = "number.json"

def ask():
    num = input("What's your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(num, f)

def answer():
    with open(filename) as f:
        num = json.load(f)
    print(f"I know your favorite number! It's {num}.")

ask()
answer()