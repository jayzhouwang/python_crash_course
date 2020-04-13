places = ['Moscow', 'Beijing', 'Tokyo', 'New York', 'London']

print("Here is the original list:")
print(places)

print("\nHere is the sorted list:")
print(sorted(places))

print("\nHere is still the original list:")
print(places)

print("\nHere is the reverse sorted list:")
print(sorted(places, reverse=True))

print("\nHere is still the original list:")
print(places)

print("\nHere is the reverse list:")
places.reverse()
print(places)

print("\nHere is the reverse list again:")
places.reverse()
print(places)

print("\nHere is the sorted list:")
places.sort()
print(places)

print("\nHere is the  reverse sorted list:")
places.sort(reverse=True)
print(places)