favourite_numbers = {
    'jack': [7, 3],
    'william': [6],
    'bill': [5, 4],
    'tom': [8, 16],
    'nancy': [0],
}
for name, nums in favourite_numbers.items():
    if len(nums) == 1:
        print(f"\n{name.title()}'s favorite number is:")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
    for num in nums:
        print(num)
