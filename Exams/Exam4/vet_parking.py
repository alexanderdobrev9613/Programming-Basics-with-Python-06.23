# user input
days = int(input())
hours = int(input())
current_price = 0
total_price = 0

# logic
for d in range(1, days + 1):
    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            current_price += 2.5
        elif d % 2 != 0 and h % 2 == 0:
            current_price += 1.25
        else:
            current_price += 1

    print(f'Day: {d} - {current_price:.2f} leva')
    total_price += current_price
    current_price = 0

# print output
print(f'Total: {total_price:.2f} leva')