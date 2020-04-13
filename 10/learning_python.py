file = "C:\\Users\\qwer\\Desktop\\share\\python code\\10\\learning_python.txt"

with open(file) as file_object:
    contents = file_object.read()
print(contents + "\n")

with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())
print()

with open(file) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())