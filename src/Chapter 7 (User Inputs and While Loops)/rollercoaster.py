# prompt the user for a height
height = input("How tall are you in inches? ")
height = int(height)

# compare input to required height to ride coaster
if height >= 48:
    print("You are tall enough to ride this ride!")
else:
    inches_left = 48 - height
    if inches_left == 1:
        print("You have to grow one more inch to ride this ride.")
    else:
        print(f"You have to grow {inches_left} more inches to ride this ride.")
