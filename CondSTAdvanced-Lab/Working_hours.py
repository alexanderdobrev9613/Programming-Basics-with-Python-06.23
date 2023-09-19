#user input
time = int(input())
day_of_week = input()
output = 'closed'

#logic
if (10 <= time <= 18) and day_of_week != 'Sunday':
    output = 'open'

#print output
print(output)