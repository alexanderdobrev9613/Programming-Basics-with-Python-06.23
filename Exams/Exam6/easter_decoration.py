#user input
customers = int(input())
basket_price = 1.5
wreath_price = 3.8
chocolate_bunny_price = 7
total_price = 0
counter = 0
end_total = 0
discounted = 0

#logic
for i in range(1, customers + 1):
    product = input()
    total_price = 0
    counter = 0

    while True:
        if product == 'Finish':
            if counter % 2 != 0:
                print(f'You purchased {counter} items for {total_price:.2f} leva.')
                end_total += total_price
            else:
                discounted = total_price - total_price * 0.2
                print(f'You purchased {counter} items for {discounted:.2f} leva.')
                end_total += discounted
            break
        else:
            if product == 'basket':
                total_price += basket_price
                counter += 1
            elif product == 'wreath':
                total_price += wreath_price
                counter += 1
            elif product == 'chocolate bunny':
                total_price += chocolate_bunny_price
                counter += 1
        product = input()



#print output
avg = end_total / customers
print(f'Average bill per client is: {avg:.2f} leva.')