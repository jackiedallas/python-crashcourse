from random import randint


class Die:
    """Representation of dice."""

    def __init__(self, sides=6):
        """Initialize die with six sides."""
        self.sides = sides

    def roll_die(self, times_to_roll):
        """Simulate rolling die."""
        increment = 1
        while increment <= times_to_roll:
            print(f"Roll {increment}: {randint(1, self.sides)}")
            increment += 1


my_die = Die()
print("Six Sided Roll")
my_die.roll_die(5)

ten_side_die = Die(sides=10)
print("\nTen Sided Roll")
ten_side_die.roll_die(5)

twenty_side_die = Die(sides=20)
print("\nTwenty Sided Roll")
twenty_side_die.roll_die(5)
