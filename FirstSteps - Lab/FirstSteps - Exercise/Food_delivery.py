chicken = int(input())
fish = int(input())
veggie = int(input())

chicken_price = 10.35
fish_price = 12.4
veggie_price = 8.15
delivery = 2.5

total_chicken = chicken * chicken_price
total_fish = fish * fish_price
total_veggie = veggie * veggie_price

total_food = total_veggie + total_fish + total_chicken

dessert = (20 / 100) * total_food

total_bill = total_food + dessert + delivery

print(total_bill)
