filename = "10/guest.txt"

name = input("Please enter your name: ")
with open(filename, "a") as file_object:
    file_object.write(name)
