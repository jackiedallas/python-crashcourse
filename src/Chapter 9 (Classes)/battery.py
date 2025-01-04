class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def set_battery_size(self, size):
        self.battery_size = size
        print(f"Setting battery size to {size}-kWh..")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = self.battery_size * 3.5
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Check if battery size is >= 65."""
        if self.battery_size < 65:
            print("Battery was less than 65-kWh, setting to 65-kWh.")
            self.battery_size = 65
        else:
            print("This battery is above the minimum size of 65.")
            print(f"Battery Size: {self.battery_size}-kWh")
