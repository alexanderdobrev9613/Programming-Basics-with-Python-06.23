#user input
budget = float(input())
season = input()
destination = ''
holiday_type = ''
price = 0 #:.2f

#logic
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = 0.3 * budget
        holiday_type = 'Camp'
    elif season == 'winter':
        price = 0.7 * budget
        holiday_type = 'Hotel'

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = 0.4 * budget
        holiday_type = 'Camp'
    elif season == 'winter':
        price = 0.8 * budget
        holiday_type = 'Hotel'
else:
    destination = 'Europe'
    if season == 'summer' or season == 'winter':
        price = 0.9 * budget
        holiday_type = 'Hotel'

#print output
print(f'Somewhere in {destination}')
print(f'{holiday_type} - {price:.2f}')
