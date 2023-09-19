#user input
name = input()
points = 0
winner_name = ''
max = 0

#logic
while True:
    if name == 'Stop':
        break
    else:
        points = 0 #tova haresva judge

    for i in range(len(name)):
        number = int(input())
        if (ord(name[i])) == number:
            points += 10
        else:
            points += 2

    if max <= points:
        max = points
        winner_name = name
    name = input()
print(f"The winner is {winner_name} with {max} points!")