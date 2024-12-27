def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit!)")
    firstName = input("First name: ")
    if firstName == 'q':
        break
    
    lastName = input("Last name: ")
    if lastName == 'q':
        break
    
    formatted_name = get_formatted_name(firstName, lastName)
    print(f"\nHello, {formatted_name}")
# name = get_formatted_name('kobe', 'bryant', 'bean')
# name2 = get_formatted_name('teena', 'marie')
# print(name)
# print(name2)