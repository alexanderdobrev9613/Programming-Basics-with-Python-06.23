#user input
points = 0
winner_name = ''
winner_points = -1
player_order = 0

#logic
while True:
    name = input()
    if name == 'Stop':
        break

    for i in range(len(name)):
        number = int(input())
        if ord(name[i]) == number:
            points += 10
        else:
            points += 2

    if points > winner_points or (points == winner_points and player_order >= 1):
        winner_name = name
        winner_points = points
        player_order += 1
        points = 0

print(f"The winner is {winner_name} with {winner_points} points!")