#user input
bad_grades_count = int(input())
problem_name = input()

average = 0
total_problems = 0
total_bad = 0
last_problem = ''

#logic
while problem_name != 'Enough':
    grade = int(input())
    total_problems += 1
    last_problem = problem_name
    average += grade
    if grade <= 4:
        total_bad += 1
        if total_bad >= bad_grades_count:
            print(f'You need a break, {bad_grades_count} poor grades.')
            break
    problem_name = input()
#print output
if problem_name == 'Enough':
    average = average / total_problems
    print(f'Average score: {average:.2f}')
    print(f'Number of problems: {total_problems}')
    print(f'Last problem: {last_problem}')