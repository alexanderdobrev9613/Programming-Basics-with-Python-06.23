#user input
name = input()
maxx = 0
hat_trick = False
winner = ''

#logic
while name != 'END':
    goals = int(input())
    if goals > maxx:
        maxx = goals
        winner = name
    if goals >= 3:
        hat_trick = True
    if goals >= 10:
        break
    name = input()

#print output
print(f'{winner} is the best player!')
if hat_trick:
    print(f'He has scored {maxx} goals and made a hat-trick !!!')
else:
    print(f'He has scored {maxx} goals.')