#user input
screening = input()
rows = int(input())
columns = int(input())
income = 0

#logic
area = rows * columns
if screening == "Premiere":
    income = area * 12
elif screening == "Normal":
    income = area * 7.5
elif screening == "Discount":
    income = area * 5

#print output
print(f'{income:.2f} leva')