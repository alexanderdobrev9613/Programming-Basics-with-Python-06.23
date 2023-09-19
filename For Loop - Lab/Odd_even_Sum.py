#user input
n = int(input())


#logic
odd_sum = 0
even_sum = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num


#print output
if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {odd_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {diff}')
