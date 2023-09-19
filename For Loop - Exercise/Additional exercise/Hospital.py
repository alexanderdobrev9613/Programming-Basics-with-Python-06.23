#user input
number_of_days = int(input())
initial_doctors = 7
daily_treated_patients = 0
daily_untreated_patients = 0

#Logic
for i in range(1, number_of_days + 1):
    daily_patients = int(input())
    if i % 3 == 0 and daily_untreated_patients > daily_treated_patients:
        initial_doctors += 1
    if daily_patients <= initial_doctors:
        daily_treated_patients += daily_patients
    else:
        daily_treated_patients += initial_doctors
        daily_untreated_patients += daily_patients - initial_doctors


#print output
print(f'Treated patients: {daily_treated_patients}.')
print(f'Untreated patients: {daily_untreated_patients}.')
