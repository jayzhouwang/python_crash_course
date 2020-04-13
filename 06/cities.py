cities = {
    'beijing': {
        'country': 'china',
        'population': 2153.6,
        'fact': 'the capital of China'
    },
    'new york': {
        'country': 'america',
        'population': 851,
        'fact': 'financial centre'
    },
    'dingyuan': {
        'country': 'china',
        'population': 97.5,
        'fact': 'the hometown of a great man'
    },
}

for city, city_info in cities.items():
    print(f"{city.title()}:")
    for key, value in city_info.items():
        print(f"\t{key}: {value}")