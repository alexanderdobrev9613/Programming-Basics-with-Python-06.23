budget = int(input())
total_expense = 0

while True:
    price = input()

    if price == 'End':
        print('You bought everything needed.')
        break

    total_expense += price
    if total_expense + price > budget:
        print('You went in overdraft!')
        break
    price = int(price)

