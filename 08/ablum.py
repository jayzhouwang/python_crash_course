def make_ablum(name, title, num=None):
    if num:
        return {
            'artist name': name.title(),
            'ablum title': title,
            'number': num}
    else:
        return {'artist name': name.title(), 'ablum title': title}


a = make_ablum('蔡依林', '舞娘')
print(a)
b = make_ablum('刘德华', '忘情水', 20)
print(b)
c = make_ablum('talor swift', 'I don\'t kown')
print(c)
