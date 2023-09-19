#user input
flowers_sort = input()
flowers_count = int(input())
budget = int(input())
flower_price = 0
roses_price = 5 * flowers_count
tulips_price = 2.8 * flowers_count
dahlias_price = 3.8 * flowers_count
narcissus_price = 3 * flowers_count
gladiolus_price = 2.5 * flowers_count


#logic
if flowers_sort == 'Roses':
    flower_price = 5
    if flowers_count > 80:
        flower_price *= 0.9
if flowers_sort == 'Dahlias':
    flower_price = 3.8
    if flowers_count > 90:
        flower_price *= 0.85
if flowers_sort == 'Tulips':
    flower_price = 2.8
    if flowers_count > 80:
        flower_price *= 0.85
if flowers_sort == 'Narcissus':
    flower_price = 3
    if flowers_count < 120:
        flower_price *= 1.15
if flowers_sort == 'Gladiolus':
    flower_price = 2.5
    if flowers_count < 80:
        flower_price *= 1.2

total_price = flower_price * flowers_count
difference = abs(total_price - budget)

#print output
if total_price <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_sort} and {difference:.2f} leva left.")
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')