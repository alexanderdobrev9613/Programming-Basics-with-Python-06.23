#user input
name = input()
wins = 0
losses = 0
total_games = 0



#logic
while name != 'End of tournaments':
    games = int(input())
    for i in range(1, games + 1):
        points_home = int(input())
        points_away = int(input())
        margin = abs(points_home - points_away)
        if points_home > points_away:
            wins += 1
            print(f'Game {i} of tournament {name}: win with {margin} points.')
        else:
            losses += 1
            print(f'Game {i} of tournament {name}: lost with {margin} points.')

    total_games += games
    name = input()


#printoutput
win_percentage = wins / total_games * 100
loss_percentage = losses / total_games * 100
if name == 'End of tournaments':
    print(f'{win_percentage:.2f}% matches win')
    print(f'{loss_percentage:.2f}% matches lost')