#user input
budget = float(input())
destination = input()
season = input()
days = int(input())
total_cost = 0


#logic
if destination == 'Dubai':
    if season == 'Winter':
        total_cost = 45000 * days
    else:
        total_cost = 40000 * days
elif destination == 'Sofia':
    if season == 'Winter':
        total_cost = 17000 * days
    else:
        total_cost = 12500 * days
elif destination == 'London':
    if season == 'Winter':
        total_cost = 24000 * days
    else:
        total_cost = 20250 * days

if destination == 'Dubai':
    total_cost -= total_cost * 0.3
elif destination == 'Sofia':
    total_cost += total_cost * 0.25

diff = abs(budget - total_cost)
#print output
if budget >= total_cost:
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')
else:
    print(f'The director needs {diff:.2f} leva more!')