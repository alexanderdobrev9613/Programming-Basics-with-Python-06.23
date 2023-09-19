#user input
heritage = float(input())
last_year_to_live = int(input())

#logic
expense_per_even = 0
age = 18
expense_per_odd = 0

for year in range(1800, last_year_to_live + 1):
    if year % 2 == 0:
        expense_per_even += 12000
        age += 1
    else:
        expense_per_odd += 12000 + (age * 50)
        age += 1

total_expense = expense_per_odd + expense_per_even
diff = abs(heritage - total_expense)

#print output
if heritage >= total_expense:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')