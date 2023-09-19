#user input
budget = float(input())
actor = input()
expense = 0

#logic
while True:
    if actor != 'ACTION':
        if len(actor) > 15:
            payment = budget * 0.2
            budget -= payment
            expense += payment
        else:
            payment = float(input())
            budget -= payment
            expense += payment
        if budget <= 0:
            print(f'We need {abs(budget):.2f} leva for our actors.')
            break
    else:
        print(f'We are left with {abs(budget):.2f} leva.')
        break
    actor = input()

#print output