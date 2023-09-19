#user input
n = int(input())

digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10

for k in range(1, digit3 + 1):
    for j in range(1, digit2 + 1):
        for i in range(1, digit1 + 1):
            result = i * j * k
            print(f"{k} * {j} * {i} = {result};")

#print output