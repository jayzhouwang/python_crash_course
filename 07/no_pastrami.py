sandwich_orders = ['tuna', 'pastrami', 'bacon',
                   'bologna', 'pastrami', 'pastrami', 'club']
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)