#user input

count_of_numbers = int(input())
sum_of_all_elements = 0
first_number = int(input())
sum_of_all_elements += first_number
max_element = first_number


#logic
for number in range(count_of_numbers - 1):
    current_element = int(input())
    sum_of_all_elements += current_element
    if current_element > max_element:
        max_element = current_element

#print output
if max_element == sum_of_all_elements - max_element:
    print('Yes')
    print(f'Sum = {max_element}')
else:
    difference = abs(max_element - (sum_of_all_elements - max_element))
    print('No')
    print(f'Diff = {difference}')