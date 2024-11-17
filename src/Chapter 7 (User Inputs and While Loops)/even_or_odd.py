# prompt the user for a number
number = int(input("Enter a number and I'll tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


new_number = int(
    input("Enter another number and I'll tell you if it's a multiple of 10: ")
    )

if new_number % 10 == 0:
    print(f"{new_number} is a multiple of 10.")
else:
    print(f"{new_number} is not a multiple of 10.")
