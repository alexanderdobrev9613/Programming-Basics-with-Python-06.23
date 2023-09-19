last_sector = input()
rows_in_first_sector = int(input())
seats_on_odd_rows = int(input())

total_seats = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    for row in range(1, rows_in_first_sector + 1):
        seats_on_current_row = seats_on_odd_rows + 2 * (row - 1) if row % 2 != 0 else seats_on_odd_rows
        for seat_num in range(1, seats_on_current_row + 1):
            total_seats += 1
            if seat_num <= 4:
                print(f"{chr(sector)}{row}{chr(96 + seat_num)}")
            else:
                break

print(total_seats)

#greshno