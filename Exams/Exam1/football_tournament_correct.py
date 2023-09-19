#user input
team = input()
played = int(input())

points = 0
wins = 0
draws = 0
losses = 0
counter = 0



#logic
while played != 0: #judge ne haresva for, iska while
    result = input()
    if result == 'W':
        wins += 1
        points += 3
    elif result == 'D':
        draws += 1
        points += 1
    elif result == 'L':
        losses += 1
    counter += 1
    if counter < played:
        continue
    else:
        win_rate = wins / played * 100
        print(f'{team} has won {points} points during this season.')
        print('Total stats:')
        print(f'## W: {wins}')
        print(f'## D: {draws}')
        print(f'## L: {losses}')
        print(f'Win rate: {win_rate:.2f}%')
        break

if played == 0:
    print(f"{team} hasn't played any games during this season.")

#print output
