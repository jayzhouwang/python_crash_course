def make_sandwich(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich('pepperoni')
make_sandwich('mushrooms', 'green peppers', 'extra cheese')
