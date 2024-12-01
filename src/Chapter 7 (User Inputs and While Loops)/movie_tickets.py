age = int(input("\nWelcome to the movies, how old are you? "))

if age < 3:
    print("Your ticket as free.")
elif age > 12:
    print("Your ticket prices is $15.")
else:
    print("Your ticket price is $10.")
