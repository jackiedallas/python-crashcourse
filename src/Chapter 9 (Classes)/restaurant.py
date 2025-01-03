import textwrap


class Restaurant:
    """Simple restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a message describing the restaurant."""
        print(textwrap.dedent(f"""
        Restaurant Name: {self.restaurant_name}
        Cuisine Type: {self.cuisine_type}
        """).strip())

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open for business!")

    def set_number_served(self, number_served):
        """Update how many customers have been served."""
        self.number_served = number_served

    def increment_number_served(self, increment):
        """Increment the number of customers that have been served."""
        if increment < 0:
            print("You can not increment negatively.")
        else:
            self.number_served += increment

    def get_number_served(self):
        """Show number of people served."""
        print(f"{self.number_served} people have been served!")


my_restaurant = Restaurant('Big Mamas', 'Southern Style')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
# print(my_restaurant.number_served)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(20)
my_restaurant.increment_number_served(15)
my_restaurant.get_number_served()
my_restaurant.increment_number_served(-1)
my_restaurant.increment_number_served(100)
my_restaurant.get_number_served()
# print(my_restaurant.number_served)
