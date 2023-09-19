#user input
cats = int(input())
small = 0
big = 0
huge = 0
total_food = 0

#logic
for i in range(1, cats + 1):
    daily_food = float(input())
    total_food += daily_food
    if 100 <= daily_food < 200:
        small += 1
    elif 200 <= daily_food < 300:
        big += 1
    elif 300 <= daily_food < 400:
        huge += 1


#print output
total_food_price = (total_food / 1000) * 12.45
print(f'Group 1: {small} cats.')
print(f'Group 2: {big} cats.')
print(f'Group 3: {huge} cats.')
print(f'Price for food per day: {total_food_price:.2f} lv.')