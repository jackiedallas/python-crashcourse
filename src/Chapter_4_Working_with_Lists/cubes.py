# make a list of the first ten cubes and use a for loop to print out the value of each cube
first_ten = list(range(1, 11))
for num in first_ten:
    cube = num**3
    print(f"{num}^3 = {cube}")