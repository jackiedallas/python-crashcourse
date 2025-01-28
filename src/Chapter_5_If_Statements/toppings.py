# create a variable for a pizza topping
available_toppings = [
    'pepperoni',
    'mushrooms',
    'green peppers',
    'extra cheese',
    'sausage',
    'olives',
    'pineapples',
    'bacon',
    'onion',
    'anchovies',
    'bbq sauce',
    'chicken'
]

requested_toppings = [
    'mushrooms',
    'french fries',
    'extra cheese'
]

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}...")
        else:
            print(f"Sorry, we don't have {requested_topping} right now.")

print("\nFinished making your Pizza!")

# # check for inequality
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")
# if requested_topping:
#     for toppings in requested_topping:
#         if toppings == 'green peppers':
#             print("Sorry, we're out of green peppers right now.")
#         else:
#             print(f"Adding {toppings}...")
# else:
#     print("Are you sure you want a plain pizza?")

# print("Finished making your pizza!")
