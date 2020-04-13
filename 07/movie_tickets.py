prompt = "Please enter your age: "
prompt += "(Enter 'quit' when you are finished.) "
flag = True
while flag:
    age = input(prompt)
    if age == 'quit':
        flag = False
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print(f"The price of your ticket is {price}.")
