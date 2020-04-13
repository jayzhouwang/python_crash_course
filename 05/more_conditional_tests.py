food = 'apple'
if food == 'apple':
    print('True')
food = 'banana'
if(food != 'apple'):
    print('False\n')

name = 'Jack'
if name.lower() == 'jack':
    print("It is!")
name = 'Tom'
if name.lower() != 'jack':
    print("It isn't!\n")

print(3 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 < 5 and 6 > 4)
print(3 > 5 or 6 > 4)

banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'
if user in banned_users:
    print(f"I am sorry, {user.title()}, you are banned!")
user = 'jack'
if user not in banned_users:
    print(f"Welcome, {user.title()}!")