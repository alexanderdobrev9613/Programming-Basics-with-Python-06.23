#User input

adults = 0
kids = 0
total_toys = 0
total_sweaters = 0

#logic
while True:
    age = input()
    if age != 'Christmas':
        age = int(age)
        if age <= 16:
            kids += 1
            total_toys += 1
        else:
            adults += 1
            total_sweaters += 1
    else:
        toys_price = total_toys * 5
        sweaters_price = total_sweaters * 15
        #print output
        print(f'Number of adults: {adults}')
        print(f'Number of kids: {kids}')
        print(f'Money for toys: {toys_price}')
        print(f'Money for sweaters: {sweaters_price}')
        break