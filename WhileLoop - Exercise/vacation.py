#user input
needed_money = float(input())
money_at_hand = float(input())
spend_days_in_a_row = 0
total_days = 0

#logic
while True:
    action = input()
    amount = float(input())
    total_days += 1
    if action == 'spend':
        spend_days_in_a_row += 1
        if amount > money_at_hand:
            money_at_hand = 0
        else:
            money_at_hand -= amount
        if spend_days_in_a_row == 5:
            print('You can\'t save the money.')
            print(total_days)
            break
    elif action == 'save':
        spend_days_in_a_row = 0
        money_at_hand += amount
        if money_at_hand >= needed_money:
            print(f'You saved the money for {total_days} days.')
            break



#print output