#user input
opened_tabs = int(input())
salary = float(input())


#Logic
for current_tab in range(opened_tabs): # same as range(1, opened_tabs + 1)
    website_name = input()
    if website_name == 'Facebook':
        salary -= 150
    elif website_name == 'Instagram':
        salary -= 100
    elif website_name == 'Reddit':
        salary -= 50

    if salary <= 0:
        break            #break ends for cycle

if salary > 0:
    print(int(salary))
else:
    print('You have lost your salary.')

#print output