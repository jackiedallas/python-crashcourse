# make a list of the multiples of 3, from 3 to 30. use a for loop to print the numbers

threes = list(range(3, 31,3))
for num in threes:
    multiple_of_three = num * 3
    print(f"{num} x 3 = {multiple_of_three}")