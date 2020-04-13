prompt = "Please enter a series of toppings:"
prompt += "\n(Enter 'quit' when you are finished.) "
flag = True
while flag:
    topping = input(prompt);
    if topping == 'quit':
        flag = False
    else:
        print(f"You'll add {topping} to your pizza.")