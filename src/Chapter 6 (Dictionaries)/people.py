alex = {
    'first_name': 'alex',
    'last_name': 'carter',
    'age': '27',
    'city': 'new york'
}
jordan = {
    'first_name': 'jordan',
    'last_name': 'lee',
    'age': '24',
    'city': 'london'
}
taylor = {
    'first_name': 'taylor',
    'last_name': 'morgan',
    'age': '63',
    'city': 'sydney'
}
casey = {
    'first_name': 'casey',
    'last_name': 'brooks',
    'age': '52',
    'city': 'toronto'
}
morgan = {
    'first_name': 'morgan',
    'last_name': 'parker',
    'age': '67',
    'city': 'berlin'
}

people = [alex, jordan, taylor, casey, morgan]

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    location = f"{person['city'].title()}"
    print(f"{full_name} is {person['age']} years old and lives in {location}.")
