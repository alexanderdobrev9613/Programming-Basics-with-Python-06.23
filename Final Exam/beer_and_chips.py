#user input
from math import ceil
name = input()
budget = float(input())
beers = int(input())
chips = int(input())

#logic
total_beer_price = beers * 1.2
total_chips_price = ceil((0.45 * total_beer_price) * chips)
total_spent = total_chips_price + total_beer_price
diff = abs(budget - total_spent)
if total_spent <= budget:
    print(f'{name} bought a snack and has {diff:.2f} leva left.')
else:
    print(f'{name} needs {diff:.2f} more leva!')

#print output