#user input
start_num = int(input())
end_num = int(input())
magic_num = int(input())
counter = 0
isfound = False

#logic
for i in range(start_num, end_num + 1):
    if isfound:
        break
    for j in range(start_num, end_num + 1):
        counter += 1
        if i + j == magic_num:
            print(f'Combination N:{counter} ({i} + {j} = {magic_num})')
            isfound = True
            break


#print output
if not isfound:
    print(f'{counter} combinations - neither equals {magic_num}')