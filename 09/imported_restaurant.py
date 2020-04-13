# import res
from rest import Restaurant as RE

my_restaurant = RE('KFC', 'fast food')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
