def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

name = get_formatted_name('kobe', 'bryant', 'bean')
name2 = get_formatted_name('teena', 'marie')
print(name)
print(name2)