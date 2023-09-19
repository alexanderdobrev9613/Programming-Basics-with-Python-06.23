from math import floor
from math import ceil

#user input
days_gone = int(input())
left_food_kg = int(input())
daily_dog_food = float(input())
daily_cat_food = float(input())
daily_tortoise_food = float(input()) / 1000

#logic
total_food = (daily_dog_food + daily_cat_food + daily_tortoise_food) * days_gone

difference = abs(left_food_kg - total_food)

if total_food <= left_food_kg:
    difference = floor(difference)
    print(f'{difference} kilos of food left.')
else:
    difference = ceil(difference)
    print(f'{difference} more kilos of food are needed.')

#print output