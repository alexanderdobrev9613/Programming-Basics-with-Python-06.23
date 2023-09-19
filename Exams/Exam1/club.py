#user input
goal = float(input())

order_price = 0
income = 0

#logic
while True:
    cocktail = input()
    if cocktail == 'Party!':
        diff = abs(goal - income)
        print(f'We need {diff:.2f} leva more.')
        break
    cocktails_per_order = int(input())
    price_cocktail = float(len(cocktail))
    order_price = cocktails_per_order * price_cocktail
    if order_price % 2 != 0:
        order_price -= (order_price * 0.25)
        income += order_price
    else:
        income += order_price
    if income >= goal:
        print('Target acquired.')
        break

#print output
print(f'Club income - {income:.2f} leva.')