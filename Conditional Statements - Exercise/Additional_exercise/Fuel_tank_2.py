#user input
fuel = input()
fuel_litres = float(input())
club_card = input()

gasoline_litre = 2.22
diesel_litre = 2.33
gas_litre = 0.93

#logic

if club_card == 'Yes':
    gasoline_litre = gasoline_litre - 0.18
    diesel_litre = diesel_litre - 0.12
    gas_litre = gas_litre - 0.08

gasoline_price = gasoline_litre * fuel_litres
diesel_price = diesel_litre * fuel_litres
gas_price = gas_litre * fuel_litres

if fuel_litres > 25:
    gasoline_price = gasoline_price - (gasoline_price * 0.1)
    gas_price = gas_price - (gas_price * 0.1)
    diesel_price = diesel_price - (diesel_price * 0.1)

elif fuel_litres >= 20:
    gasoline_price = gasoline_price - (gasoline_price * 0.08)
    gas_price = gas_price - (gas_price * 0.08)
    diesel_price = diesel_price - (diesel_price * 0.08)

if fuel == 'Gas':
    print(f'{gas_price:.2f} lv.')
elif fuel == 'Gasoline':
    print(f'{gasoline_price:.2f} lv.')
elif fuel == 'Diesel':
    print(f'{diesel_price:.2f} lv.')




#print output
