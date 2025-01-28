''' a buffet style restaurant offers only five basic foods, think of five foods
and store them in a tuple'''

base_foods = ('burgers', 'fries', 'wraps', 'salad', 'pasta')

# use a for loop to print each food the restaurant offers
print("My restaurant offers:\n")
for food in base_foods:
    print(f"{food.title()}")

base_foods = ('burritos', 'fries', 'enchiladas', 'salad', 'pasta')

print("\nMy restaurant's new menu is:\n")
for food in base_foods:
    print(f"{food.title()}")
