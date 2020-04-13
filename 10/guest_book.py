filename = "10/guest_book.txt"

with open(filename, 'a') as file_object:
    while True:
        print("Please Enter your name:")
        name = input("Enter 'q' to quit: ")
        if name == 'q':
            break
        else:
            file_object.write(name + "\n")
