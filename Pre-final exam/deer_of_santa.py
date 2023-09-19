#user input
from math import floor
from math import ceil


days = int(input())
starting_food = int(input())
first_deer_daily = float(input())
second_deer_daily = float(input())
third_deer_daily = float(input())

#logic
total_food_eaten = (first_deer_daily + second_deer_daily + third_deer_daily) * days
diff = abs(starting_food - total_food_eaten)

#print output
if starting_food >= total_food_eaten:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')