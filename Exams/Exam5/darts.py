#user input
name = input()
multiplier = input()
target = 301
successful = 0
unsuccessful = 0


#logic
while multiplier != 'Retire':
    points = int(input())
    if multiplier == 'Double':
        points *= 2
    elif multiplier == 'Triple':
        points *= 3
    if points > 301:
        unsuccessful += 1
    elif 0 < points < 301:
        successful += 1
    if points == 0:
        successful += 1
        print(f'{name} won the leg with {successful} shots')
        break
    multiplier = input()

#print output
if multiplier == 'Retire':
    print(f'{name} retired after {unsuccessful} unsuccessful shots.')