# create a function with two arguments
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")


describe_pet(animal_type='poodle', pet_name='roxie')
describe_pet(animal_type='dog', pet_name='joe')
describe_pet(pet_name='bruce', animal_type='shark')
describe_pet(pet_name='willie')
