import textwrap


class Restaurant:
    """Simple restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a message describing the restaurant."""
        print(textwrap.dedent(f"""
        Restaurant Name: {self.restaurant_name}
        Cuisine Type: {self.cuisine_type}
        """).strip())

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open for business!")


my_restaurant = Restaurant('Big Mamas', 'Southern Style')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
