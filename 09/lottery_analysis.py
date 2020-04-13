from random import choices

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'e', 'i', 'o', 'u']
my_ticket = [1, 3, 1, 4]
count = 0

while True:
    count += 1

    prize = []
    for i in range(4):
        prize.append(choices(list)[0])

    if my_ticket == prize:
        print(count)
        break
