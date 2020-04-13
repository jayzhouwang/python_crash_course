class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the information of the restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"This is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print("The restaurant is open.")


my_restaurant = Restaurant('KFC', 'fast food')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
