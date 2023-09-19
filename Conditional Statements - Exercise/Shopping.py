#userinput

budget = float(input())
number_of_videocards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

#logic
total_price_of_videocard = number_of_videocards * 250
price_of_processor = total_price_of_videocard * 0.35
price_of_ram = total_price_of_videocard * 0.1

total_price_of_processors = price_of_processor * number_of_processors
total_price_of_ram = price_of_ram * number_of_ram

total_sum = total_price_of_ram + total_price_of_processors + total_price_of_videocard

if number_of_videocards > number_of_processors:
    total_sum *= 0.85

difference = abs(total_sum - budget)

if total_sum <= budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")

#print output

