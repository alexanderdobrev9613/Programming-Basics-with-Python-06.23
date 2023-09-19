#user input
from math import floor

breed = input()
gender = input()
life = 0
is_valid = True

#logic
if gender == 'm':
    if breed == 'British Shorthair':
        life += 13
    elif breed == 'Siamese':
        life += 15
    elif breed == 'Persian':
        life += 14
    elif breed == 'Ragdoll':
        life += 16
    elif breed == 'American Shorthair':
        life += 12
    elif breed == 'Siberian':
        life += 11
    else:
        is_valid = False
        print(f'{breed} is invalid cat!')
elif gender == 'f':
    if breed == 'British Shorthair':
        life += 14
    elif breed == 'Siamese':
        life += 16
    elif breed == 'Persian':
        life += 15
    elif breed == 'Ragdoll':
        life += 17
    elif breed == 'American Shorthair':
        life += 13
    elif breed == 'Siberian':
        life += 12
    else:
        is_valid = False
        print(f'{breed} is invalid cat!')

life_months = (life * 12) / 6

#print output
if is_valid:
    print(f'{floor(life_months)} cat months')
