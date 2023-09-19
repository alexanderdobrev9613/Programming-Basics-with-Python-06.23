#user input
students = int(input())
top = 0 #5 do 6
very_good = 0 #4 do 5
good = 0 #3 do 4
fail = 0 #2 do 3
total_grades = 0

#logic
for i in range(students):
    grade = float(input())
    if grade >= 5:
        top += 1
    elif 4 <= grade <= 4.99:
        very_good += 1
    elif 3 <= grade <= 3.99:
        good += 1
    else:
        fail += 1
    total_grades += grade

top_percentage = top / students * 100
very_good_percentage = very_good / students * 100
good_percentage = good / students * 100
fail_percentage = fail / students * 100
average = total_grades / students


#print output
print(f'Top students: {top_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {very_good_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {good_percentage:.2f}%')
print(f'Fail: {fail_percentage:.2f}%')
print(f'Average: {average:.2f}')