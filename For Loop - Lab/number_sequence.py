#user input
n = int(input())

#logic
user_input = int(input())
min_num = user_input
max_num = user_input

for i in range(n - 1):
    num = int(input())
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

#print output
print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
