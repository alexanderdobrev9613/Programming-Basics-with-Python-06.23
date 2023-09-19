#user_input
fuel = input()
tank = float(input())

#logic
if fuel != 'Diesel' and fuel != 'Gasoline' and fuel != 'Gas':
    print('Invalid fuel!')

elif tank >= 25:
    print(f'You have enough {fuel.lower()}.')
else:
    print(f'Fill your tank with {fuel.lower()}!')

#print output