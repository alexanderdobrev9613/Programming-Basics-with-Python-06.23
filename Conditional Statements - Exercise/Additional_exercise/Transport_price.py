#user input
kilometers = int(input())
time_of_day = input()

#logic
taxi_base = 0.7
taxi_day_km = 0.79
taxi_night_km = 0.9
taxi_day_price = taxi_base + (taxi_day_km * kilometers)
taxi_night_price = taxi_base + (taxi_night_km * kilometers)

bus_price = 0.09 * kilometers

train_price = 0.06 * kilometers

if kilometers < 20:
    if time_of_day == 'day':
        print(f'{taxi_day_price:.2f}')
    elif time_of_day == 'night':
        print(f'{taxi_night_price:.2f}')

elif kilometers < 100:
    print(f'{bus_price:.2f}')

else:
    print(f'{train_price:.2f}')



#print output