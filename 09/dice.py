from random import randint

class Die:
    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        print(randint(1, self.sides))

my_die = Die()
for i in range(10):
    my_die.roll_die()

print()

my_die.sides = 10
for i in range(10):
    my_die.roll_die()

print()

my_die.sides = 20
for i in range(10):
    my_die.roll_die()
