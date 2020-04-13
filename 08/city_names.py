def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'


print(city_country('dingyuan', 'china'))
print(city_country('london', 'britain'))
print(city_country('new york', 'america'))
