"""
addition.py
@author: Jackie Johnson-Dallas
Created January 28th, 2025
This script will prompt for numerical inputs adds them together, and prints
the results. It will also catch the "ValueError" if either input value is not
a number, and print a friendly error message.
"""

print("Enter two numbers and I will give you the sum.\n")
print("Enter 'q' to quit.\n")

while True:
    firstNum = input("First number: ")
    if firstNum == 'q':
        break
    secondNum = input("Second number: ")
    if secondNum == 'q':
        break
    try:
        sum = float(firstNum) + float(secondNum)
        result = round(sum, 2)
    except ValueError:
        print("Invalid input, be sure to only enter whole numbers.")
    else:
        print(f"{firstNum} + {secondNum} = {result}\n")
