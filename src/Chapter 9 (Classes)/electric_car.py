from car import Car


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


class ElectricCar(Car):
    """Represent aspects of a car, specific to EV's."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
        # self.battery_size = 0

    # def set_battery_size(self, size):
    #     self.battery_size = size
    #     print(f"Setting battery size to {size}-kWh..")

    # def describe_battery(self):
    #     """Print statement describing the battery size."""
    #     print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.set_battery_size(75)
my_tesla.battery.describe_battery()
# my_tesla.set_battery_size(75)
# my_tesla.describe_battery()
