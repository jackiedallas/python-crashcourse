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


# my_new_car = Car('subaru', 'impreza', 2017)
# print(my_new_car.get_descriptive_name())
# # my_new_car.odometer_reading = 500
# my_new_car.update_odometer(100)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(100)
# my_new_car.increment_odometer(-50)
# # my_new_car.increment_odometer(-500)
# # my_new_car.update_odometer(500)
# # my_new_car.update_odometer(100)
# my_new_car.read_odometer()
