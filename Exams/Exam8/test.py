#user input
capacity = float(input())
bag = input()
counter = 0

#logic
while bag != 'End':
    bag = float(bag)
    capacity -= bag
    if counter % 3 == 0:
        bag += bag * 0.1
    if capacity <= 0:
        print(f'No more space!')
        print(f'Statistic: {counter} suitcases loaded.')
        break
    counter += 1
    bag = input()

#ptintoutput
if bag == 'End':
    print(f'Congratulations! All suitcases are loaded!')
    print(f'Statistic: {counter} suitcases loaded.')