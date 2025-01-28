# prompt user for their name
name = input("Please enter your name: ")
print(f"Hello, {name.title()}!")

# build a prompt over several lines
last_name = "If you share your last name we can personalize"
last_name += "\nthe message you see. Please enter your last name: "
full_name = f"{name} {input(last_name)}"
print(f"Hello, {full_name.title()}!")

age = input(f"How old are you {full_name.title()}: ")
age = int(age)
if age >= 21:
    print(f"{full_name.title()} you are old enough to drink!")
else:
    years_left = 21 - age
    print(f"You have {years_left} years left before you can enjoy a drink.")
