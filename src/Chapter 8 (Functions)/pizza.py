def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    # print(toppings)
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'pepperoni')
make_pizza(16, 'cheese', 'mushrooms', 'pineapples')