budget = int(input())
total_expense = 0

while total_expense <= budget:
    price = input()
    if price == 'End':
        print(f'You bought everything needed.')
        break
    else:
        price = int(price)
        total_expense += price
if total_expense > budget:
    print(f'You went in overdraft!')