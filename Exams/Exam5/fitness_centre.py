#user input
people = int(input())
workout = 0
protein = 0
back = 0
chest = 0
abs = 0
legs = 0
shake = 0
bar = 0

#logic
for i in range(1, people + 1):
    activity = input()
    if activity == 'Back':
        back += 1
        workout += 1
    elif activity == 'Chest':
        chest += 1
        workout +=1
    elif activity == 'Abs':
        abs += 1
        workout +=1
    elif activity == 'Legs':
        legs += 1
        workout +=1
    elif activity == 'Protein shake':
        shake += 1
        protein += 1
    elif activity == 'Protein bar':
        bar += 1
        protein += 1

workout_percentage = workout / people * 100
protein_percentage = protein / people * 100
print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{shake} - protein shake')
print(f'{bar} - protein bar')
print(f'{workout_percentage:.2f}% - work out')
print(f'{protein_percentage:.2f}% - protein')


#print output