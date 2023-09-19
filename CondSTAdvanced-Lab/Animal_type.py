#user input
animal = input()
output = 'unknown'

#logic
if animal == 'dog':
    output = 'mammal'
elif animal == 'snake' or animal == 'tortoise' or animal == 'crocodile':
    output = 'reptile'

#print output
print(output)