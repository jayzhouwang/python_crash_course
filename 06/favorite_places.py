favorite_places = {
    'jack': ['dingyuan', 'nanjing'],
    'wiliiam': ['beijing', 'shanghai', 'guangzhou'],
    'ada': ['new york'],
}
for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
    else:
        print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")