import json


def get_stored_number():
    """Get stored number if available."""
    filename = "number.json"
    try:
        with open(filename) as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num


def get_new_num():
    """Prompt for a new number."""
    num = input("What's your favorite number? ")
    filename = "number.json"
    with open(filename, 'w') as f:
        json.dump(num, f)
    return num


def great():
    num = get_stored_number()
    if num:
        print(f"I know your favorite number! It's {num}.")
    else:
        num = get_new_num()
        print(f"We'll remember your favorite number when you come back!")


great()
