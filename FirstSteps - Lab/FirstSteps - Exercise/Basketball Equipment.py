annual_tax = int(input())

sneakers = annual_tax - ((40 / 100) * annual_tax)
kit = sneakers - ((20 / 100) * sneakers)
ball = kit / 4
accessories = ball / 5

total_expense = annual_tax + sneakers + kit + ball + accessories

print(total_expense)
