#user input
men = int(input())
women = int(input())
max_tables = int(input())
count = 0


#logic
for m in range(1, men + 1):
    for f in range(1, women + 1):
        if count == max_tables:
            break

        print(f'({m} <-> {f})', end=" ")
        count +=1


#print output

