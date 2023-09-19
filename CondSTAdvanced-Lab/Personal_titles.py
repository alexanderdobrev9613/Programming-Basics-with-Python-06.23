#user input
age = float(input())
gender = input()


#logic
if age < 16 and gender == 'f':
    output = 'Miss'
if age >= 16 and gender == 'f':
    output = 'Ms.'
if age < 16 and gender == 'm':
    output = 'Master'
if age >= 16 and gender == 'm':
    output = 'Mr.'


#print output
print(output)