# create a prompt to get a city the user has been to
prompt = "\nPlease enter the name of a city you've visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

# create a while loop and use break to refactor parrot program
# a while loop that starts with 'True' will run forever unless
# it reaches a break statement
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}!")
