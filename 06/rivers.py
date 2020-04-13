rivers = {
    'nile': 'egypt',
    'amazon river': 'brazil',
    'changjiang river': 'china',
}
for river, country in rivers.items():
    print(f"The {river.title()} runs though {country.title()}.")

for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())