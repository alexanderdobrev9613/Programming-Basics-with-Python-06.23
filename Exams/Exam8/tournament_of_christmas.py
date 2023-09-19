#user input
days = int(input())
wins = 0
losses = 0
income = 0
win_days = 0
lose_days = 0
whole_income = 0


#logic
for i in range(days):
    wins = 0
    losses = 0
    income = 0
    while True:
        sport = input()
        if sport == 'Finish':
            break
        result = input()
        if result == 'win':
            wins += 1
            income += 20
        elif result == 'lose':
            losses += 1

    if wins > losses:
        income += income * 0.1
        whole_income += income
        win_days += 1
    else:
        lose_days += 1
        whole_income += income

if win_days > lose_days:
    whole_income += whole_income * 0.2
    print(f'You won the tournament! Total raised money: {whole_income:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {whole_income:.2f}')



#print output