#user input
start = int(input())
end = int(input())


#logic
for digit1 in range(start, end + 1):
    for digit2 in range(start, end + 1):
        for digit3 in range(start, end + 1):
            for digit4 in range(start, end + 1):
                if digit1 % 2 != digit4 % 2 and digit1 > digit4 and (digit2 + digit3) % 2 == 0:
                    print(f'{digit1}{digit2}{digit3}{digit4}', end=' ')
