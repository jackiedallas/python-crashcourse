"""
city_functions.py
@author: Jackie Johnson-Dallas
This script will define a function that accepts two parameters, a city and 
country name. The function should return a single string of the form 
City, Country, such as Santiago, Chile. 
"""

def get_formatted_location(city, country, population=''):
    """Generate formatted city, country format"""
    if population:
        pop_int = int(population)
        formatted_location = f"{city}, {country} - Population: {pop_int.__format__(',.0f')}"
    else:
        formatted_location = f"{city}, {country}"
    return formatted_location.title()

print(get_formatted_location('aviano', 'italy'))
print(get_formatted_location('paris', 'france', '686000000'))   