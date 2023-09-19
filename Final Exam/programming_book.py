#user input
price_per_page = float(input())
price_per_cover = float(input())
discount = int(input())
price_designer = float(input())
percent_team = int(input())

#logic
total_pages_price = 899 * price_per_page
total_covers_price = 2 * price_per_cover
printing = total_covers_price + total_pages_price
print_discounted = printing - (printing * (discount / 100))
post_designer = print_discounted + price_designer
paid_by_team = post_designer * (percent_team / 100)
money = post_designer - paid_by_team


#print output
print(f'Avtonom should pay {money:.2f} BGN.')