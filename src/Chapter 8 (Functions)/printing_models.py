def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

# start with some designs that need to be printed
unprinted_designs = ['yoga mat', 'television', 'monster truck']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)