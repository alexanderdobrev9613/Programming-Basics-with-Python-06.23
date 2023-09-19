#user input
from math import floor

number_of_tournaments = int(input())
starting_points = int(input())
total_points = 0
tournaments_won = 0

#logic

for tournament in range(number_of_tournaments):
    stage = input()
    if stage == 'W':
        total_points += 2000
        tournaments_won += 1
    elif stage == 'F':
        total_points += 1200
    elif stage == 'SF': #moje i else
        total_points += 720

average_points = floor(total_points / number_of_tournaments)  # moje i s floor(total_points / number_of_tournaments iliii total_points // number_of_tournaments
total_points += starting_points
percentage_of_won_tournaments = tournaments_won / number_of_tournaments * 100

#print output
print(f'Final points: {total_points:}')
print(f'Average points: {average_points}')
print(f'{percentage_of_won_tournaments:.2f}%')