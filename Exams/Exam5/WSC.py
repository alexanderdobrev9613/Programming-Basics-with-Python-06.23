#user input
leg = input()
ticket = input()
count_ticket = int(input())
trophy_photo = input()
price = 0

#logic
if leg == 'Quarter final':
    if ticket == 'Standard':
        price += count_ticket * 55.5
    elif ticket == 'Premium':
        price += count_ticket * 105.2
    elif ticket == 'VIP':
        price += count_ticket * 118.9
elif leg == 'Semi final':
    if ticket == 'Standard':
        price += count_ticket * 75.88
    elif ticket == 'Premium':
        price += count_ticket * 125.22
    elif ticket == 'VIP':
        price += count_ticket * 300.4
elif leg == 'Final':
    if ticket == 'Standard':
        price += count_ticket * 110.1
    elif ticket == 'Premium':
        price += count_ticket * 160.66
    elif ticket == 'VIP':
        price += count_ticket * 400

price_trophy = 40 * count_ticket
if price > 4000:
    price_trophy = 0
    price -= price * 0.25
elif 2500 < price <= 4000:
    price -= price * 0.1


if trophy_photo == 'Y':
    print(f'{(price_trophy + price):.2f}')
else:
    print(f'{price:.2f}')

#print output
