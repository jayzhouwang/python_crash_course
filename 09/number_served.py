class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the information of the restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"This is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, num):
        """Set the served number of the restuaurant"""
        self.number_served = num

    def increment_number_served(self, incre):
        """Add the given amount to the number served"""
        self.number_served += incre


restaurant = Restaurant('KFC', 'fast food')

print(restaurant.number_served)

restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(15)
print(restaurant.number_served)

restaurant.increment_number_served(50)
print(restaurant.number_served)
