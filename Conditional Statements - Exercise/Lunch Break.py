from math import ceil

#userinput
series_name = input()
episode_time = int(input())
lunch_break= int(input())

#logic
eating_time = lunch_break / 8
rest_time = lunch_break / 4

time_to_watch = lunch_break - (eating_time + rest_time)
time_remaining_after_watching = (ceil(abs(time_to_watch - episode_time)))

if time_to_watch >= episode_time:
    print(f"You have enough time to watch {series_name} and left with {time_remaining_after_watching} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {time_remaining_after_watching} more minutes.")

#print output
