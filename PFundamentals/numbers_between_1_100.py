num = float(input())

while 1 > num or 100 < num:
    num = float(input())
print(f'The number {num:.2f} is between 1 and 100')