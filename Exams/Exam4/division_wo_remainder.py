#user input
count = int(input())
two = 0
three = 0
four = 0


#logic
for i in range(count):
    n = int(input())
    if n % 2 == 0:
        two += 1
    if n % 3 == 0:
        three += 1
    if n % 4 == 0:
        four += 1

two_percentage = two / count * 100
three_percentage = three / count * 100
four_percentage = four / count * 100

#print output
print(f'{two_percentage:.2f}%')
print(f'{three_percentage:.2f}%')
print(f'{four_percentage:.2f}%')