def make_ablum(name, title):
    return {'artist name': name.title(), 'ablum title': title}


while True:
    print("(enter 'q' at any time to quit)")
    name = input("name: ")
    if name == 'q':
        break
    title = input("title: ")
    if title == 'q':
        break
    print(make_ablum(name, title))
