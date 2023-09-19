#user input
day = input()

output = 'Error'

#logic
if day == 'Monday':
    output = 'Working day'
elif day == 'Tuesday':
    output = 'Working day'
elif day == 'Wednesday':
    output = 'Working day'
elif day == 'Thursday':
    output = 'Working day'
elif day == 'Friday':
    output = 'Working day'
elif day == 'Saturday':
    output = 'Weekend'
elif day == 'Sunday':
    output = 'Weekend'

#print output
print(output)