#user input
budget = float(input())
series_count = int(input())
total_price = 0
diff = 0

#logic
for i in range(series_count):
    name = input()
    price = float(input())
    if name == 'Thrones':
        price -= price * 0.5
        total_price += price
    elif name == 'Lucifer':
        price -= price * 0.4
        total_price += price
    elif name == 'Protector':
        price -= price * 0.3
        total_price += price
    elif name == 'TotalDrama':
        price -= price * 0.2
        total_price += price
    elif name == 'Area':
        price -= price * 0.1
        total_price += price
    else:
        total_price += price

    diff = abs(total_price - budget)
if total_price > budget:
    print(f'You need {diff:.2f} lv. more to buy the series!')
else:
    print(f'You bought all the series and left with {diff:.2f} lv.')

#print output