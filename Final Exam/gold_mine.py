#user input
locations = int(input())


#logic
current_gold = 0

for i in range(1, locations + 1):
    expected_av_daily_gold = float(input())
    days_per_location = int(input())
    days = 0
    current_gold = 0
    for k in range(1, days_per_location + 1):
        days += 1
        daily_gold = float(input())
        current_gold += daily_gold
        av_daily_gold = current_gold / days_per_location
        if days == days_per_location:
            if av_daily_gold >= expected_av_daily_gold:
                print(f'Good job! Average gold per day: {av_daily_gold:.2f}.')
            else:
                diff = abs(av_daily_gold - expected_av_daily_gold)
                print(f'You need {diff:.2f} gold.')
        else:
            continue



#print output