# prompt the user for pizza toppings
prompt = "\nWhat toppings do you want on your pizza: "
prompt += "\n(When you're done enter 'quit'.) "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I will add {topping.title()} to your pizza.")
