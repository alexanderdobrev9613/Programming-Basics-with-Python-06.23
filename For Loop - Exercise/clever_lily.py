#user input
ages = int(input())
laundry_price = float(input())
price_per_toy = (int(input()))
total_toys = 0
total_money = 0
current_birthday_money = 0

#logic
for birthday in range (1, ages + 1):
    if birthday % 2 == 0: #even birthday
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else: #odd birthday if birthday % 2 != 0:
        total_toys += 1

total_money += total_toys * price_per_toy

#print output
difference = abs(total_money - laundry_price)
if total_money >= laundry_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')