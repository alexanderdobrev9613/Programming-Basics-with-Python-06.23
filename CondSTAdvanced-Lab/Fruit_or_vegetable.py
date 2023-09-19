#user input
product = input()
output = 'unknown'


#logic
if product == 'banana' or product == 'apple' or product == 'kiwi' or\
        product == 'cherry' or product == 'lemon' or product == 'grapes':
    output = 'fruit'

if product == 'tomato' or product == 'cucumber' or product == 'pepper' or\
    product == 'carrot':
    output = 'vegetable'

#print output
print(output)