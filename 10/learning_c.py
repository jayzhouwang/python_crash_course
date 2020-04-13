file = "C:\\Users\\qwer\\Desktop\\share\\python code\\10\\learning_python.txt"

with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    msg = line.strip().replace('Python', 'C')
    print(msg)