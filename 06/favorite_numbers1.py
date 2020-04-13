names = ['jack', 'william', 'bill', 'tom', 'nancy']
favourite_numbers = {
    names[0]: 7,
    names[1]: 6,
    names[2]: 3,
    names[3]: 8,
    names[4]: 0,
}
for i in range(5):
    print(f"{names[i].title()}'s favourite number is {favourite_numbers[names[i]]}.")

favourite_numbers = {
    'jack': 7,
    'william': 6,
    'bill': 3,
    'tom': 8,
    'nancy': 0,
}
for name, num in favourite_numbers.items():
    print(f"{name.title()}'s favourite number is {num}.")
