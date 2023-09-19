#user input
fruit = input()
day_of_week = input()
qty = float(input())
price = 0
is_input_correct = True

#logic
if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or \
    day_of_week == 'Thursday' or day_of_week == 'Friday':

    if fruit == 'banana':
        price = qty * 2.5
    elif fruit == 'apple':
        price = qty * 1.2
    elif fruit == 'orange':
        price = qty * 0.85
    elif fruit == 'grapefruit':
        price = qty * 1.45
    elif fruit == 'kiwi':
        price = qty * 2.7
    elif fruit == 'pineapple':
        price = qty * 5.5
    elif fruit == 'grapes':
        price = qty * 3.85
    else:
        is_input_correct = False

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':

    if fruit == 'banana':
        price = qty * 2.7
    elif fruit == 'apple':
        price = qty * 1.25
    elif fruit == 'orange':
        price = qty * 0.9
    elif fruit == 'grapefruit':
        price = qty * 1.6
    elif fruit == 'kiwi':
        price = qty * 3
    elif fruit == 'pineapple':
        price = qty * 5.6
    elif fruit == 'grapes':
        price = qty * 4.2
    else:
        is_input_correct = False

else:
    is_input_correct = False

#print output
if is_input_correct:
    print(f'{price:.2f}')
else:
    print('error')