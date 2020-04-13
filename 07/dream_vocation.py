responses = {}
polling_active = True

while polling_active:
    name = input("What's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
    for name, response in responses.items():
        print(f"{name.strip().title()} wants to visit {response.strip().title()}.")
