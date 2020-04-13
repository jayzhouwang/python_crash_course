my_pizzas = ['kfc', 'McDonald', 'pizzahut']
friend_pizzas = my_pizzas[:]
my_pizzas.append('laoxiangji')
friend_pizzas.append('dekeshi')
print(f"My favorite pizzas are:\n{my_pizzas}")
print(f"My friend's favorite pizzas are:\n{friend_pizzas}")
for pizza in friend_pizzas:
    print(pizza)