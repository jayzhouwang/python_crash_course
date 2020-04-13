favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

candicates = ['phil', 'jen', 'tom', 'sarah', 'jack', 'edward']
for name in candicates:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take the poll.")
         