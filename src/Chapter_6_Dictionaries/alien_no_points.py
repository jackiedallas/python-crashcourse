# create alien dictionary with no points
alien_0 = {'color': 'green', 'speed': 'slow'}

# get points key using the print method should throw "KeyError: 'points'"
# print(alien_0['points'])

# you can use the get() method to set default values if key doesn't exist
point_value = alien_0.get('points', 'No points scored.')

print(point_value)
