# create an empty dictionary called 'responses'
responses = {}

# set a flag to indicate the polling is active
polling_active = True

# create while loop to start the program
while polling_active:
    # prompt for user name and response
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the dictionary
    responses[name] = response

    # check if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
