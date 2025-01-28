"""
city_functions.py
@author: Jackie Johnson-Dallas
This script will define a function that accepts two parameters, a city and 
country name. The function should return a single string of the form 
City, Country, such as Santiago, Chile. 
"""

def get_formatted_location(city, country):
    """Generate formatted city, country format"""
    formatted_location = f"{city}, {country}"
    return formatted_location.title()
    