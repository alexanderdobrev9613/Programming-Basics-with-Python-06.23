#user input
count = int(input())
type = input()
delivery = input()
price = 0

#logic
if type == '90X130':
    price += 110 * count
    if 30 < count <= 60:
        price -= price * 0.05
    elif count > 60:
        price -= price * 0.08
elif type == '100X150':
    price += 140 * count
    if 40 < count <= 80:
        price -= price * 0.06
    elif count > 80:
        price -= price * 0.1
elif type == '130X180':
    price += 190 * count
    if 20 < count <= 50:
        price -= price * 0.07
    elif count > 50:
        price -= price * 0.12
elif type == '200X300':
    price += 250 * count
    if 25 < count <= 50:
        price -= price * 0.09
    elif count > 50:
        price -= price * 0.14

if delivery == 'With delivery':
    price += 60
if count > 99:
    price -= price * 0.04


#print output
if count >= 10:
    print(f'{price:.2f} BGN')
else:
    print('Invalid order')