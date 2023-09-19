from math import ceil

#user input
count_people = int(input())
entry_fee = float(input())
price_lounger = float(input())
price_umbrella = float(input())

#logic
total_entry = count_people * entry_fee
total_umbrella = ceil(count_people / 2) * price_umbrella
total_loungers = ceil(count_people - (count_people / 4)) * price_lounger
end_sum = total_loungers + total_umbrella + total_entry


#print output
print(f'{end_sum:.2f} lv.')