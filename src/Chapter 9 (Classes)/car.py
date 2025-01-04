class Car:
    """A representation of a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print statement showing mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("You can't increment with negative miles.")
        else:
            self.odometer_reading += miles


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


class ElectricCar(Car):
    """Represent aspects of a car, specific to EV's."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")
