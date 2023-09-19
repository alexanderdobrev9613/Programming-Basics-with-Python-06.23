#user input
days_off = int(input())

#logic
play_norm_minutes_per_year = 30000
play_minutes_per_working_day = 63
play_minutes_per_day_off = 127

working_days = 365 - days_off
total_play_minutes_working = working_days * play_minutes_per_working_day
total_play_minutes_off = days_off * play_minutes_per_day_off
total_play_minutes = total_play_minutes_off + total_play_minutes_working

difference = abs(total_play_minutes - play_norm_minutes_per_year)

hours = difference // 60
minutes = difference % 60

if total_play_minutes > play_norm_minutes_per_year:
    print('Tom will run away')
    print(f'{hours:.0f} hours and {minutes:.0f} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours:.0f} hours and {minutes:.0f} minutes less for play')



#print output