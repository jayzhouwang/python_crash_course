def read_file(filename):
    try:
        with open(filename) as f:
            cats = f.read()
    except FileNotFoundError:
        pass
    else:
        print(cats.strip())


files = ["10/cats.txt", "10/dogs.txt"]
for file in files:
    read_file(file)
