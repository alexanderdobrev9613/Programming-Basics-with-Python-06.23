#input
first_athlete = int(input())
second_athlete = int(input())
third_athlete = int(input())

#logic
sum_time = first_athlete + second_athlete + third_athlete
minutes = sum_time // 60
seconds = sum_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
