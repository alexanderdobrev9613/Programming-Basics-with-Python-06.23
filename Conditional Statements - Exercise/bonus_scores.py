#user input
number = int(input())
bonus = 0
#logic
if number <= 100:
    bonus = 5
elif number >= 1000:
    bonus = number * 0.1
else:
    bonus = number * 0.2
if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2

final_sum = bonus + number
#print user output

print(f"{bonus}")
print(f"{final_sum}")
