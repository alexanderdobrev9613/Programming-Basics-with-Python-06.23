#user input
guests = int(input())
price_per_guest = float(input())
budget = float(input())

#logic
if 10 <= guests <= 15:
    price_per_guest -= price_per_guest * 0.15
elif 15 < guests <= 20:
    price_per_guest -= price_per_guest * 0.2
elif guests > 20:
    price_per_guest -= price_per_guest * 0.25

cake = budget * 0.1
total_price = price_per_guest * guests + cake
diff = abs(total_price - budget)

#print output
if total_price <= budget:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {diff:.2f} leva needed.')