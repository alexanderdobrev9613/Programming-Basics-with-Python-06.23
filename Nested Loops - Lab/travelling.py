#user input
saved_money = 0

#logic
while True:
    destination = input()
    if destination == 'End':
        break
    else:
        min_budget = float(input())
        saved_money = 0
        while True:
            income = float(input())
            saved_money += income
            if saved_money >= min_budget:
                print(f'Going to {destination}!')
                break
