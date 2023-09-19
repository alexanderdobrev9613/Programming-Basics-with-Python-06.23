from math import floor
from math import ceil

#user input

price_magnolia = int(input()) * 3.25
price_hyacinth = int(input()) * 4
price_rose = int(input()) * 3.5
price_cactus = int(input()) * 8
price_gift = float(input())

#logic
total_income = (price_cactus + price_hyacinth + price_rose + price_magnolia)
total_income_after_tax = total_income - (total_income * 0.05)
difference = abs(total_income_after_tax - price_gift)

if total_income_after_tax < price_gift:
    difference = ceil(difference)
    print(f'She will have to borrow {difference:.0f} leva.')
else:
    difference = floor(difference)
    print(f'She is left with {difference:.0f} leva.')


#print output