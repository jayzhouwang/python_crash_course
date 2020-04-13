class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the information of the restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"This is a {self.cuisine_type} restaurant.\n")

    def open_restaurant(self):
        print("The restaurant is open.\n")


restaurant1 = Restaurant('KFC', 'fast food')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('Macdonod', 'fast food')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Laoxiangji', 'Chinese food')
restaurant3.describe_restaurant()

