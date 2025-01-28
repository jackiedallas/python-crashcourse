from city_functions import get_formatted_location

def test_city_country():
    """Should return a city, country like 'Aviano, Italy'."""
    formatted_location = get_formatted_location('aviano', 'italy')
    assert formatted_location == 'Aviano, Italy'

def test_city_country_population():
    """Should return 'City, Country - Population: xxx'"""
    formatted_location = get_formatted_location(
        'aviano', 
        'italy', 
        '2348949029480'
        )
    assert formatted_location == 'Aviano, Italy - Population: 2,348,949,029,480'