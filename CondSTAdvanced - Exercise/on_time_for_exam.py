# User input
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

# Logic
exam_time = (exam_hour * 60) + exam_minute
arrival_time = (arrival_hour * 60) + arrival_minute

diff = arrival_time - exam_time

if diff > 0:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif diff >= -30:
    print("On time")
    if diff != 0:
        print(f"{abs(diff)} minutes before the start")
elif diff < -30:
    print("Early")
    if abs(diff) < 60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hours = abs(diff) // 60
        minutes = abs(diff) % 60
        print(f"{hours}:{minutes:02d} hours before the start")