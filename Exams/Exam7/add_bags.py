#user input
price_above_20kg = float(input())
kg_luggage = float(input())
days_left = int(input())
luggage_count = int(input())
price = 0

#logic
if kg_luggage < 10:
    price += (price_above_20kg * 0.2) * luggage_count
elif 10 <= kg_luggage <= 20:
    price += (price_above_20kg / 2) * luggage_count
if kg_luggage > 20:
    price += price_above_20kg * luggage_count
if days_left > 30:
    price += price * 0.1
elif 7 <= days_left <= 30:
    price += price * 0.15
elif days_left < 7:
    price += price * 0.4


#print output
print(f'The total price of bags is: {price:.2f} lv. ')