#user input
name = input()
successful = 0
unsuccessful = 0
score = 0


#logic
while True:
    multiplier = input()

    if multiplier == 'Retire':
        print(f'{name} retired after {unsuccessful} unsuccessful shots.')
        break
    else:
        points = int(input())
        if multiplier == 'Double':
            points *= 2
        elif multiplier == 'Triple':
            points *= 3
        score += points
        if score > 301:
            score -= points
            unsuccessful += 1
        elif 0 < score < 301:
            successful += 1
        if score == 301:
            successful += 1
            print(f'{name} won the leg with {successful} shots.')
            break


#print output
