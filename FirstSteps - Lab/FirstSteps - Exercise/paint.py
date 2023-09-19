nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags = 0.40

total_nylon = (nylon + 2) * nylon_price
total_paint = (paint * 1.1) * paint_price
total_thinner = thinner * thinner_price

total_materials = total_thinner + total_paint + total_nylon + bags

labour_per_hour = total_materials * (30 / 100)

all_total = total_materials + labour_per_hour * hours

print(all_total)
