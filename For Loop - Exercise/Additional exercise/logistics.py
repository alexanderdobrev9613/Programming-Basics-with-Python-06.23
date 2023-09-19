#user input
stock_per_vehicle = int(input())
bus_per_ton = 200
truck_per_ton = 175
train_per_ton = 120
price_bus = 0
price_truck = 0
price_train = 0
price = 0
total_tons = 0

bus_tons = 0
truck_tons = 0
train_tons = 0


#logic
for i in range(stock_per_vehicle): #moje bi ot 0 i +1
    tons = int(input())
    if tons <= 3:
        bus_tons += tons
    elif 4 <= tons <= 11:
        truck_tons += tons
    else:
        train_tons += tons
    total_tons += tons


price_train = train_per_ton * train_tons
price_truck = truck_per_ton * truck_tons
price_bus = bus_per_ton * bus_tons
price = price_bus + price_train + price_truck


average_price = price / total_tons
bus_ton_percentage = bus_tons / total_tons * 100
truck_ton_percentage = truck_tons / total_tons * 100
train_ton_percentage = train_tons / total_tons * 100
#print output
print(f'{average_price:.2f}')
print(f'{bus_ton_percentage:.2f}%')
print(f'{truck_ton_percentage:.2f}%')
print(f'{train_ton_percentage:.2f}%')