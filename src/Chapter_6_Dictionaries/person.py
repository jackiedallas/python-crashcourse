# use a dictionary to store info about a person you know
# people = {
#     'yakla' == {
#         'first_name': 'yakla',
#         'last_name': 'dallas',
#         'age': '28',
#         'city': 'locust grove'
#     },
#     'jackie' == {
#         'first_name': 'jackie',
#         'last_name': 'dallas',
#         'age': '32',
#         'city': 'locust grove'
#     }
# }

yakla = {
    'first_name': 'yakla',
    'last_name': 'laddas',
    'age': '82',
    'city': 'miami'
    }

# people['yakla']

firstName = yakla['first_name'].title()
lastName = yakla['last_name'].title()
age = yakla['age']
city = yakla['city'].title()

# print each information about the person
print(f"{firstName} {lastName} is {age} years old. She lives in {city}, VA.")

fav_num = {
    'yakla': '8',
    'dackson': '24',
    'simot': '10',
    'cakmen': '32',
    'jax': '23'
    }

for key, value in fav_num.items():
    person = key.title()
    favNum = value
    print(f"{person}'s favorite number is {favNum}.")
