def count_string(filename, str):
    try:
        with open(filename, encoding='utf8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist. ")
    else:
        num = text.lower().count(str)
        print(f"The number of the string '{str}' in {filename} is {num}.")


files = ['10/alice.txt', '10/little_women.txt', '10/moby_dick.txt']

for file in files:
    count_string(file, 'the')
    count_string(file, 'the ')
