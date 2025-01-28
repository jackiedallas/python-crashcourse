from city_functions import get_formatted_location

def test_city_country():
    """Should return a city, country like 'Aviano, Italy'."""
    formatted_location = get_formatted_location('aviano', 'italy')
    assert formatted_location == 'Aviano, Italy'