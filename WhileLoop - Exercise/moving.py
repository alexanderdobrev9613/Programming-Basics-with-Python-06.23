#user input
free_width = int(input())
free_length = int(input())
free_height = int(input())
boxes = input()
total_space = free_width * free_height * free_length


#logic
while boxes != 'Done':
    boxes = int(boxes)
    if boxes <= total_space:
        total_space -= boxes
    else:
        diff = abs(total_space - boxes)
        print(f'No more free space! You need {diff} Cubic meters more.')
        break
    boxes = input()

#print output
if boxes == 'Done':
    print(f'{total_space} Cubic meters left.')