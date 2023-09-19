#user input
price_of_holiday = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

#logic
price_puzzles = number_puzzles * 2.6
price_dolls = number_dolls * 3
price_bears = number_bears * 4.1
price_minions = number_minions * 8.2
price_trucks = number_trucks * 2
total_sum_of_toys = price_puzzles + price_dolls + price_bears + price_minions + price_trucks
total_number_of_toys = number_trucks + number_minions + number_bears + number_dolls + number_puzzles

if total_number_of_toys >= 50:
    total_sum_of_toys *= 0.75 #total_sum_of_toys = total_sum_of_toys - (total_sum_of_toys * 25/100)

total_sum_of_toys *= 0.9 # total_sum_of_toys = total_sum_of_toys - (total_sum_of_toys * 10/100)
money_left = abs(total_sum_of_toys - price_of_holiday)

if total_sum_of_toys >= price_of_holiday:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_left:.2f} lv needed.")

#print output

