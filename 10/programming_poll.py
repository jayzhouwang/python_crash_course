filename = "10/reasons.txt"

with open(filename, 'a') as file_object:
    while True:
        print("Please Enter your reason:")
        reason = input("Enter 'q' to quit: ")
        if reason == 'q':
            break
        else:
            file_object.write(reason + "\n")
