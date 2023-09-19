#user input
budget = float(input())
total_price = 0
product = input()
count_of_products = 0

#logic
while product != 'Stop':
    product_price = float(input())
    count_of_products += 1
    if count_of_products % 3 == 0:
        product_price -= (product_price / 2)
        total_price += product_price
    else:
        total_price += product_price
    if total_price > budget:
        diff = abs(budget - total_price)
        print(f"You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break
    product = input()


#print output
if product == 'Stop':
    print(f'You bought {count_of_products} products for {total_price:.2f} leva.')