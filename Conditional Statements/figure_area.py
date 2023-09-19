from math import pi

#read user input

figure = input()

area = 0

# logic
if figure == 'square':
    a = float(input())
    area = a * a
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif figure == 'circle':
    r = float(input())
    area = pi * r * r
elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = (a * h) / 2

#print output
print(f'{area:.3f}')