# user input
turns = int(input())
o_to_nine = 0
ten_to_nineteen = 0
twenty_to_twentynine = 0
thirty_to_thirtynine = 0
forty_to_fifty = 0
invalid = 0
score = 0

# logic
for i in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        o_to_nine += 1
        score += number * 0.2
    elif 10 <= number <= 19:
        ten_to_nineteen += 1
        score += number * 0.3
    elif 20 <= number <= 29:
        twenty_to_twentynine += 1
        score += number * 0.4
    elif 30 <= number <= 39:
        thirty_to_thirtynine += 1
        score += 50
    elif 40 <= number <= 50:
        forty_to_fifty += 1
        score += 100
    else:
        invalid += 1
        score /= 2

p1 = o_to_nine / turns * 100
p2 = ten_to_nineteen / turns * 100
p3 = twenty_to_twentynine / turns * 100
p4 = thirty_to_thirtynine / turns * 100
p5 = forty_to_fifty / turns * 100
p6 = invalid / turns * 100

# print output
print(f'{score:.2f}')
print(f'From 0 to 9: {p1:.2f}%')
print(f'From 10 to 19: {p2:.2f}%')
print(f'From 20 to 29: {p3:.2f}%')
print(f'From 30 to 39: {p4:.2f}%')
print(f'From 40 to 50: {p5:.2f}%')
print(f'Invalid numbers: {p6:.2f}%')

