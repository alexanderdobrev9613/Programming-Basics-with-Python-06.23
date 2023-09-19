current_pages = int(input())

pages_per_hour = int(input())

days = int(input())

total_time_for_book = current_pages / pages_per_hour

hours_per_day = (current_pages / pages_per_hour) / days

print(int(hours_per_day))
