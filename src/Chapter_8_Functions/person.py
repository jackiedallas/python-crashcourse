# define a function that returns dictionary
def build_person(firstName, lastName, age=None):
    """Return dictionary about the person"""
    person = {'first': firstName, 'last': lastName}
    if age:
        person['age'] = age
    return person

kobe = build_person('kobe', 'bryant', 27)
print(kobe)