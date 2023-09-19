veg_price = float(input())
fruit_price = float(input())
total_veg_kg = float(input())
total_fruit_kg = float(input())

euro = 1.94

total_veg_price = veg_price * total_veg_kg
total_fruit_price = fruit_price * total_fruit_kg
whole_price_euro = (total_veg_price + total_fruit_price) / euro

print(f'{whole_price_euro: .2f}')
