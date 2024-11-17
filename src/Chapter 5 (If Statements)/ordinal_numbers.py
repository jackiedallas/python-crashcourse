# store the numbers 1 - 9 in a list
nums = range(1, 10)

for value in nums:
    if value == 1:
        print('1st')
    elif value == 2:
        print('2nd')
    elif value == 3:
        print('3rd')
    else:
        print(f"{value}th")
