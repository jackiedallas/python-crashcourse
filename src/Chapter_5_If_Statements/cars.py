# create a list of cars
cars = ['audi', 'bmw', 'subaru', 'chevrolet']

# loop through the cars list and print the names with the title method
# bmw should be all caps
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
