from random import choices

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'e', 'i', 'o', 'u']

prize = []
for i in range(4):
    prize.append(choices(list)[0])

print("Any ticket matching these four numbers or letters wins a prize:")
print(f"{prize[0]} {prize[1]} {prize[2]} {prize[3]} ")
