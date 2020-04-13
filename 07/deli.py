# Start with sandwiches that need to be made,
# and an empty list to hold finished sandwiches.
sandwich_orders = ['tuna', 'bacon', 'bologna', 'club']
finished_sandwiches = []

#Make each sandwiches until there are no more sandwiches orders.
# Move each finished sandwich into the list of finished_sandwiches.
while sandwich_orders:
    kind = sandwich_orders.pop()
    print(f"I made your {kind} sandwich.")
    finished_sandwiches.append(kind)

# Display all finished sandwiched.
print("\nFinished sandwiched:")
for sandwich in finished_sandwiches:
    print(sandwich)

#this program should use FIFO
#but we just imitate confirmed_users.py