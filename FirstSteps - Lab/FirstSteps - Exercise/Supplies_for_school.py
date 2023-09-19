pens_pack = int(input())
markers_pack = int(input())
cleaner_litre = int(input())
discount_percent = int(input())

pen_price = 5.8
marker_price = 7.2
cleaner_price = 1.2

total_price = (pens_pack * pen_price) + (markers_pack * marker_price) + (cleaner_litre * cleaner_price)

total_discounted_price = total_price - (total_price * (discount_percent/100))

print(total_discounted_price)
