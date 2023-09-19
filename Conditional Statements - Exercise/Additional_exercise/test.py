from math import ceil
from math import floor


# user input
area_sm = int(input())
grape_for_sm = float(input())
needed_wine_litres = int(input())
number_of_workers = int(input())

# logic
total_grape = area_sm * grape_for_sm
total_wine = (4 / 10) * (total_grape / 2.5)
difference = abs(total_wine - needed_wine_litres)
wine_liters_per_worker = difference / number_of_workers

if total_wine >= needed_wine_litres:
    total_wine = floor(total_wine)
    difference = ceil(difference)
    wine_liters_per_worker = ceil(wine_liters_per_worker)
    print(f'Good harvest this year! Total wine: {total_wine:.0f} liters.')
    print(f'{difference:.0f} liters left -> {wine_liters_per_worker:.0f} liters per person.')
else:
    difference = floor(difference)
    print(f'It will be a tough winter! More {difference:.0f} liters wine needed.')

# print output