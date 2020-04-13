my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for my in my_foods:
    print(my)

print("\nMy friend's favorite foods are:")
for fr in friend_foods:
    print(fr)
