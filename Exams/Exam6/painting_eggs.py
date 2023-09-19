#user input
egg_size = input()
egg_color = input()
packs = int(input())
total_income = 0


#logic
if egg_color == 'Red':
    if egg_size == 'Large':
        total_income += packs * 16
    elif egg_size == 'Medium':
        total_income += packs * 13
    elif egg_size == 'Small':
        total_income += packs * 9

elif egg_color == 'Green':
    if egg_size == 'Large':
        total_income += packs * 12
    elif egg_size == 'Medium':
        total_income += packs * 9
    elif egg_size == 'Small':
        total_income += packs * 8

elif egg_color == 'Yellow':
    if egg_size == 'Large':
        total_income += packs * 9
    elif egg_size == 'Medium':
        total_income += packs * 7
    elif egg_size == 'Small':
        total_income += packs * 5


#print output
total_end = total_income - (0.35 * total_income)
print(f'{total_end:.2f} leva.')