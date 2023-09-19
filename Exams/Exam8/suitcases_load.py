#user input
capacity = float(input())
bag = input()
taken_space = 0
counter = 0

#logic
while bag != 'End':
    bag = float(bag)
    if counter > 0 and counter % 3 == 0:
        bag += bag * 0.1
    taken_space += bag
    if capacity >= taken_space:
        counter += 1
    else:
        print(f'No more space!')
        print(f'Statistic: {counter} suitcases loaded.')
        break
    bag = input()

#ptintoutput
if bag == 'End':
    print(f'Congratulations! All suitcases are loaded!')
    print(f'Statistic: {counter} suitcases loaded.')