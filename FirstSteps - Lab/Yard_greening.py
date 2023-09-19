square_meters = float(input())

price_meter = 7.61

final_price = (square_meters * price_meter) - (square_meters * price_meter) * (18/100)

discount = (18/100) * (square_meters * price_meter)

print(f'The final price is: {final_price} lv.')

print(f'The discount is: {discount} lv.')
