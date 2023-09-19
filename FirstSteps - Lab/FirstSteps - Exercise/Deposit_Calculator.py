deposit_amount = float(input())

months = int(input())

year_interest = float(input())

interest = deposit_amount * year_interest / 100

monthly_interest = interest / 12

end_total = deposit_amount + months * monthly_interest

print(end_total)
