pet1 = {
    'kind': 'dog',
    'owner': 'tom',
}

pet2 = {
    'kind': 'cat',
    'owner': 'jerry',
}

pet3 = {
    'kind': 'pig',
    'owner': 'william',
}

pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"The pet's kind is a {pet['kind']}, and the pet's owner is {pet['owner'].title()}.")