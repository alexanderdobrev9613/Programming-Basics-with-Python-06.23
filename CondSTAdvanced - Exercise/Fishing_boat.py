#user input
budget = int(input())
season = input()
fishermen = int(input())
rent_price = 0

#logic
if season == 'Spring':
    rent_price = 3000
    if fishermen <= 6:
        rent_price = rent_price - (rent_price * 0.1)
    elif 7 <= fishermen <= 11:
        rent_price = rent_price - (rent_price * 0.15)
    elif fishermen >= 12:
        rent_price = rent_price - (rent_price * 0.25)

elif season == 'Summer':
    rent_price = 4200
    if fishermen <= 6:
        rent_price = rent_price - (rent_price * 0.1)
    elif 7 <= fishermen <= 11:
        rent_price = rent_price - (rent_price * 0.15)
    elif fishermen >= 12:
        rent_price = rent_price - (rent_price * 0.25)

elif season == 'Autumn':
    rent_price = 4200
    if fishermen <= 6:
        rent_price = rent_price - (rent_price * 0.1)
    elif 7 <= fishermen <= 11:
        rent_price = rent_price - (rent_price * 0.15)
    elif fishermen >= 12:
        rent_price = rent_price - (rent_price * 0.25)

elif season == 'Winter':
    rent_price = 2600
    if fishermen <= 6:
        rent_price = rent_price - (rent_price * 0.1)
    elif 7 <= fishermen <= 11:
        rent_price = rent_price - (rent_price * 0.15)
    elif fishermen >= 12:
        rent_price = rent_price - (rent_price * 0.25)

if fishermen % 2 == 0 and season != 'Autumn':
    rent_price = rent_price - (rent_price * 0.05)

difference = abs(budget - rent_price)

#print output
if budget >= rent_price:
    print (f'Yes! You have {difference:.2f} leva left.')
else:
    print (f'Not enough money! You need {difference:.2f} leva.')