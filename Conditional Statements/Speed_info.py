#read user input
speed = float(input())

#logic
if speed <=10:
    print('slow')
elif speed <=50:
    print('average')
elif speed <=150:
    print('fast')
elif speed <=1000:
    print('ultra fast')
else:
    print('extremely fast')

#print output
