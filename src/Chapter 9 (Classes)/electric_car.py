from car import Car
from battery import Battery


class ElectricCar(Car):
    """Represent aspects of a car, specific to EV's."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.set_battery_size(20)
my_tesla.battery.get_range()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# my_tesla.set_battery_size(75)
# my_tesla.describe_battery()
