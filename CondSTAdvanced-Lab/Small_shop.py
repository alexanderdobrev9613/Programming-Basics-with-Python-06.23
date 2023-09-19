#user input
product = input()
town = input()
qty = float(input())
price = 0

#logic
if town == 'Sofia':
    if product == 'coffee':
        price = qty * 0.5
    elif product == 'water':
        price = qty * 0.8
    elif product == 'beer':
        price = qty * 1.2
    elif product == 'sweets':
        price = qty * 1.45
    elif product == 'peanuts':
        price = qty * 1.6

elif town == 'Plovdiv':
    if product == 'coffee':
        price = qty * 0.4
    elif product == 'water':
        price = qty * 0.7
    elif product == 'beer':
        price = qty * 1.15
    elif product == 'sweets':
        price = qty * 1.3
    elif product == 'peanuts':
        price = qty * 1.5

elif town == 'Varna':
    if product == 'coffee':
        price = qty * 0.45
    elif product == 'water':
        price = qty * 0.7
    elif product == 'beer':
        price = qty * 1.1
    elif product == 'sweets':
        price = qty * 1.35
    elif product == 'peanuts':
        price = qty * 1.55



#print output
print(price)
