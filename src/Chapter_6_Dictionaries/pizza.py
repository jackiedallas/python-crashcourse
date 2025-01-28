# store information about a pizza order
pizza = {
    'crust': 'thick',
    'toppings': [
        'mushrooms',
        'pepperoni',
        'extra cheese'
    ]
}

# summarize the order
print(f"""You ordered a {pizza['crust'].title()}-Crust Pizza with
the following toppings:""")

for topping in pizza['toppings']:
    print(f"\t{topping.title()}")
