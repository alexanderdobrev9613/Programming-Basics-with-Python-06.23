#user input
month = input()
nights = int(input())
studio_price_per_night = 0
apartment_price_per_night = 0

#logic

if month == 'May' or month == 'October':
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 8 <= nights <= 14:
        studio_price_per_night = studio_price_per_night - (studio_price_per_night * 0.05)
    elif nights > 14:
        studio_price_per_night = studio_price_per_night - (studio_price_per_night * 0.3)
        apartment_price_per_night = apartment_price_per_night - (apartment_price_per_night * 0.1)

if month == 'June' or month == 'September':
    studio_price_per_night = 75.2
    apartment_price_per_night = 68.7
    if nights > 14:
        studio_price_per_night = studio_price_per_night - (studio_price_per_night * 0.2)
        apartment_price_per_night = apartment_price_per_night - (apartment_price_per_night * 0.1)

if month == 'July' or month == 'August':
    studio_price_per_night = 76
    apartment_price_per_night = 77
    if nights > 14:
        apartment_price_per_night = apartment_price_per_night - (apartment_price_per_night * 0.1)

total_studio = studio_price_per_night * nights
total_apartment = apartment_price_per_night * nights

print(f'Apartment: {total_apartment:.2f} lv.')
print(f'Studio: {total_studio:.2f} lv.')


#print output