# create a simple dictionary
alien_0 = {'color': 'green', 'points': 5}

# print color and points
# print(alien_0['color'])
# print(alien_0['points'])

# add x and y coordinates to the alien dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# print(alien_0)

alien_1 = {}

alien_1['color'] = 'purple'
alien_1['points'] = 10

# print(alien_1)

alien_0['speed'] = 'medium'

print(f"Original Position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
