#logic

step_goal = 10000
total_steps = 0

while total_steps < step_goal:
    command = input()
    if command == 'Going home':
        last_steps = int(input())
        total_steps += last_steps
        break
    command = int(command)
    total_steps += command
diff = abs(total_steps - step_goal)

#print output
if total_steps >= step_goal:
    print('Goal reached! Good job!')
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")