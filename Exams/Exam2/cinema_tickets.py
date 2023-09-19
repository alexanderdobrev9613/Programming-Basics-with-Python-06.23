#user input
movie_name = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
seats_taken = 0

#logic
while movie_name != 'Finish':
    free_seats = int(input())
    ticket_type = input()
    while ticket_type != 'End':
        if ticket_type == 'student':
            student_tickets += 1
            seats_taken += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
            seats_taken += 1
        elif ticket_type == 'kid':
            kid_tickets += 1
            seats_taken += 1
        if seats_taken == free_seats:
            break
        ticket_type = input()

    percentage_capacity = seats_taken / free_seats * 100
    print(f'{movie_name} - {percentage_capacity:.2f}% full.')
    seats_taken = 0
    movie_name = input()

#print output
total_tickets = kid_tickets + standard_tickets + student_tickets
student_percentage = student_tickets / total_tickets * 100
standard_percentage = standard_tickets / total_tickets * 100
kid_percentage = kid_tickets / total_tickets * 100
print(f'Total tickets: {total_tickets}')
print(f'{student_percentage:.2f}% student tickets.')
print(f'{standard_percentage:.2f}% standard tickets.')
print(f'{kid_percentage:.2f}% kids tickets.')
