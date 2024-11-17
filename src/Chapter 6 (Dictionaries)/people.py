alex = {
    'first_name': 'alex',
    'last_name': 'carter',
    'age': '27',
    'location': {
        'city': 'new york',
        'country': 'usa'
    }
}
jordan = {
    'first_name': 'jordan',
    'last_name': 'lee',
    'age': '24',
    'location': {
        'city': 'london',
        'country': 'united kingdom'
    }
}
taylor = {
    'first_name': 'taylor',
    'last_name': 'morgan',
    'age': '63',
    'location': {
        'city': 'sydney',
        'country': 'australia'
    }
}
casey = {
    'first_name': 'casey',
    'last_name': 'brooks',
    'age': '52',
    'location': {
        'city': 'toronto',
        'country': 'canada'
    }
}
morgan = {
    'first_name': 'morgan',
    'last_name': 'parker',
    'age': '67',
    'location': {
        'city': 'berlin',
        'country': 'germany'
    }
}

people = [alex, jordan, taylor, casey, morgan]

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    city = person['location']['city']
    country = person['location']['country']
    if country == 'usa':
        print(f"{full_name} is {person['age']} years old and lives in {city.title()}, {country.upper()}.")
    else:
        country.title()
        print(f"{full_name} is {person['age']} years old and lives in {city.title()}, {country.title()}.")
