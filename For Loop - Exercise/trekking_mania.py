#it's like histogram

#user input
number_of_groups = int(input())

people_Musala = 0
people_Monblan = 0
people_Kilimandjaro = 0
people_K2 = 0
people_Everest = 0

#logic
for group in range(number_of_groups):
    people_per_group = int(input())
    if people_per_group <= 5:
        people_Musala += people_per_group
    elif 6 <= people_per_group <= 12:
        people_Monblan += people_per_group
    elif 13 <= people_per_group <= 25:
        people_Kilimandjaro += people_per_group
    elif 26 <= people_per_group <= 40:
        people_K2 += people_per_group
    elif people_per_group >= 41:
        people_Everest += people_per_group

    total_people = people_K2 + people_Kilimandjaro + people_Everest + people_Musala + people_Monblan

    Musala_percentage = people_Musala / total_people * 100
    Monblan_percentage = people_Monblan / total_people * 100
    Kilimandjaro_percentage = people_Kilimandjaro / total_people * 100
    K2_percentage = people_K2 / total_people * 100
    Everest_percentage = people_Everest / total_people * 100

#print output
print(f'{Musala_percentage:.2f}%')
print(f'{Monblan_percentage:.2f}%')
print(f'{Kilimandjaro_percentage:.2f}%')
print(f'{K2_percentage:.2f}%')
print(f'{Everest_percentage:.2f}%')