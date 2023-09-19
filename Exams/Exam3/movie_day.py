#user input
total_needed_time = int(input())
scenes = int(input())
scene_duration = int(input())



#logic
preparation = 0.15 * total_needed_time
total_actual_time = preparation + (scenes * scene_duration)
diff = round(abs(total_needed_time - total_actual_time))

if total_actual_time <= total_needed_time:
    print(f'You managed to finish the movie on time! You have {diff} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {diff} minutes.')


#print output
