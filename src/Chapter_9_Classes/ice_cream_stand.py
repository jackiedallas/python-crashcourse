from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to ice cream."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def set_flavors(self, *flavors):
        """Add flavors from the list of flavors"""
        for flavor in flavors:
            self.flavors.append(flavor)

    def describe_flavors(self):
        """Print list of flavors available."""
        print("Available Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


my_ice_cream_stand = IceCreamStand('Ritas', 'gelato')
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.open_restaurant()
my_ice_cream_stand.set_flavors('peach', 'apple')
my_ice_cream_stand.describe_flavors()
my_ice_cream_stand.set_flavors('mango', 'strawberry', 'blueberry', 'lime')
my_ice_cream_stand.describe_flavors()
my_ice_cream_stand.increment_number_served(15)
my_ice_cream_stand.increment_number_served(5)
my_ice_cream_stand.get_number_served()
