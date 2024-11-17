# make a dictionary containing 3 major rivers
rivers = {'nile': 'egypt', 'danube': 'germany', 'amazon': 'brazil'}

# print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")
