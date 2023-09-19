#user input
beverage = input()
sugar = input()
drink_count = int(input())

price = 0

#logic
if beverage == 'Espresso':
    if sugar == 'Without':
        price = 0.9 * drink_count
    elif sugar == 'Normal':
        price = drink_count
    elif sugar == 'Extra':
        price = 1.2 * drink_count
elif beverage == 'Cappuccino':
    if sugar == 'Without':
        price = 1* drink_count
    elif sugar == 'Normal':
        price = 1.2 * drink_count
    elif sugar == 'Extra':
        price = 1.6 * drink_count
elif beverage == 'Tea':
    if sugar == 'Without':
        price = 0.5 * drink_count
    elif sugar == 'Normal':
        price = 0.6 * drink_count
    elif sugar == 'Extra':
        price = 0.7 * drink_count

if sugar == 'Without':
    price -= price * 0.35
if beverage == 'Espresso' and drink_count >= 5:
    price -= price * 0.25
if price > 15:
    price -= price * 0.2

print(f'You bought {drink_count} cups of {beverage} for {price:.2f} lv.')