#user input
max_first_number = int(input())
max_second_number = int(input())
max_third_number = int(input())



#logic
for digit1 in range(2, max_first_number + 1, 2):
    for digit2 in range(2, max_second_number + 1):
        if digit2 == 2 or digit2 == 3 or digit2 == 5 or digit2 == 7:
            for digit3 in range(2, max_third_number + 1, 2):
                print(f'{digit1} {digit2} {digit3}')



#printoutput