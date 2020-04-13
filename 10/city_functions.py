# def format(city, country):
#     return f"{city.title()}, {country.title()}"
    
# def format(city, country, population):
#     return f"{city.title()}, {country.title()}, - population {population}"

def format(city, country, population=''):
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
