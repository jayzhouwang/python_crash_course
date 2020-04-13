guest_list = ['Einstein', 'Newton', 'Euler', 'Mao']
print(f"{guest_list[0]}, can you hava a dinner with me?")
print(f"{guest_list[1]}, can you hava a dinner with me?")
print(f"{guest_list[2]}, can you hava a dinner with me?")
print(f"{guest_list[3]}, can you hava a dinner with me?\n")

print(f"{guest_list[3]} cannot come!\n")

guest_list[3] = 'Xi'
print(f"{guest_list[0]}, can you hava a dinner with me?")
print(f"{guest_list[1]}, can you hava a dinner with me?")
print(f"{guest_list[2]}, can you hava a dinner with me?")
print(f"{guest_list[3]}, can you hava a dinner with me?\n")

print("Good news, I have found a bigger table, so we can invite more people!\n")

guest_list.insert(0, 'Hu')
guest_list.insert(2, 'Jiang')
guest_list.append('Deng')

print(f"{guest_list[0]}, can you hava a dinner with me?")
print(f"{guest_list[1]}, can you hava a dinner with me?")
print(f"{guest_list[2]}, can you hava a dinner with me?")
print(f"{guest_list[3]}, can you hava a dinner with me?")
print(f"{guest_list[4]}, can you hava a dinner with me?")
print(f"{guest_list[5]}, can you hava a dinner with me?")
print(f"{guest_list[6]}, can you hava a dinner with me?\n")

print("Sorry, I can invite only 2 people for dinner.\n")

name = guest_list.pop()
print(f"{name}, I'm so sorry that I can't invite you to my dinner.")
name = guest_list.pop()
print(f"{name}, I'm so sorry that I can't invite you to my dinner.")
name = guest_list.pop()
print(f"{name}, I'm so sorry that I can't invite you to my dinner.")
name = guest_list.pop()
print(f"{name}, I'm so sorry that I can't invite you to my dinner.")
name = guest_list.pop()
print(f"{name}, I'm so sorry that I can't invite you to my dinner.\n")

print(f"{guest_list[0]}, you're still invited!")
print(f"{guest_list[1]}, you're still invited!\n")

del guest_list[0]
#print(guest_list)
del guest_list[0] #del guest_list[0]之后，原来的 guest_list[1] 就变成了新的 guest_list[0]

print(guest_list)