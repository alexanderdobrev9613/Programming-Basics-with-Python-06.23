#user input
first_player_eggs = int(input())
second_player_eggs = int(input())
winner = input()

#logic
while winner != 'End':
    if winner == 'one':
        second_player_eggs -= 1
    elif winner == 'two':
        first_player_eggs -= 1
    if first_player_eggs == 0 or second_player_eggs == 0:
        break
    winner = input()

#print output
if winner == 'End':
    print(f'Player one has {first_player_eggs} eggs left.')
    print(f'Player two has {second_player_eggs} eggs left.')
if first_player_eggs == 0:
    print(f'Player one is out of eggs. Player two has {second_player_eggs} eggs left.')
elif second_player_eggs == 0:
    print(f'Player two is out of eggs. Player one has {first_player_eggs} eggs left.')