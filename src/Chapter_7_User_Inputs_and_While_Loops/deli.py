# create a list called sandwich_orders
sandwich_orders = [
    'classic club',
    'pastrami',
    'italian caprese',
    'spicy buffalo chicken',
    'pastrami',
    'philly cheese steak',
    'ham and cheese',
    'pastrami'
]

finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# print(sandwich_orders)
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I finished your {current_sandwich.title()} Sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} Sandwich")
