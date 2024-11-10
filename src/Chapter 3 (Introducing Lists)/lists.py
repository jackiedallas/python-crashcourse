# In python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
special_bike = bicycles[2].title()
message = f"My first bike was a {special_bike}"

# python will print it's interpretation of a list including the square brackets if you print it the way we do below.
print(bicycles)

# print only the first element of the list ('trek')
print(bicycles[0])

# print the first element and use the title method to capitalize it, making it look more formal
print(bicycles[0].title())

# print the last element ('specialized') of the list
print(bicycles[-1].title())

print(message)

