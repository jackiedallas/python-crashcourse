def city_country(city, country):
    """Return city country pair neatly formatted"""
    if country == 'us' or country == 'usa':
        location = f"{city.title()}, {country.upper()}"
    else:
        location = f"{city.title()}, {country.title()}"
    return location

while True:
    print("\nWhere would you like to visit someday:")
    print("(Enter 'q' at any time to quit)")
    
    city = input("City: ")
    if city == 'q':
        break
    country = input("Country: ")
    if country == 'q':
        break
    
    place_to_visit = city_country(city, country)
    print(f"\n{place_to_visit} sounds like an amazing location!")