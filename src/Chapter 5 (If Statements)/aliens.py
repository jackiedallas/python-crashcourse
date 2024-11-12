# create a variable called alien_color and assign it a value
alien_color_green = 'green'
alien_color_red = 'red'
alien_color_yellow = 'yellow'

aliens = ['green', 'yellow', 'red', 'green', 'orange']

for color in aliens:
    if color == alien_color_green:
        print("Player just earned 5 points")
    elif color == alien_color_red:
        print("Player just earned 10 points")
    elif color == alien_color_yellow:
        print("Player earned 1 point")
    else:
        print("Player earned no points")
