# user input
months = int(input())
monthly_water = 20
monthly_internet = 15
water = monthly_water * months
internet = monthly_internet * months
electricity = 0
other = 0

# logic
for i in range(months):
    monthly_electricity = float(input())
    electricity += monthly_electricity
    other += (monthly_electricity + monthly_water + monthly_internet) * 1.2

total_expense = electricity + water + internet + other
average_expense = total_expense / months

# print output
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average_expense:.2f} lv")