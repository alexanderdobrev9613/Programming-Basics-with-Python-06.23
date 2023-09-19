#user input
from math import ceil
count = int(input())
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0


#logic
for k in range(1, count + 1):
    sugar_g_used = int(input())
    flour_g_used = int(input())
    if sugar_g_used > max_sugar:
        total_sugar += sugar_g_used
        max_sugar = sugar_g_used
    else:
        total_sugar += sugar_g_used

    if flour_g_used > max_flour:
        total_flour += flour_g_used
        max_flour = flour_g_used
    else:
        total_flour += flour_g_used

#print output
needed_sugar = ceil(total_sugar / 950)
needed_four = ceil(total_flour / 750)
print(f'Sugar: {needed_sugar}')
print(f'Flour: {needed_four}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')