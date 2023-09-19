#user input
budget = float(input())
nights = int(input())
price_per_night = float(input())
percentage_additional_expense = int(input())

#logic

additional_expense = budget * percentage_additional_expense / 100
if nights > 7:
    price_per_night -= 0.05 * price_per_night

total_nights = nights * price_per_night
end_sum = total_nights + additional_expense
diff = abs(budget - end_sum)
if budget >= end_sum:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')



#print output