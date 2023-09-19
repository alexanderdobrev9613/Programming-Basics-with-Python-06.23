#user input
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
movie_name = input()

#logic
while movie_name != 'Finish':
    free_seats = int(input())
    sold_seats = 0
    for free_ticket in range(free_seats): #free ticket sa bileti koito mogat da se kupqt / svobodni
        current_ticket = input() #student / kid/ standard
        if current_ticket == 'End':
            break
        elif current_ticket == 'student':
            student_tickets += 1
        elif current_ticket == 'standard':
            standard_tickets += 1
        elif current_ticket == 'kid': #else
            kid_tickets += 1
        sold_seats += 1
    percentage_full_hall = sold_seats / free_seats * 100
    print(f'{movie_name} - {percentage_full_hall:.2f}% full.')
    movie_name = input()

#print output
total_sold_tickets = student_tickets + kid_tickets + standard_tickets
percentage_student_tickets = student_tickets / total_sold_tickets * 100
percentage_standard_tickets = standard_tickets / total_sold_tickets * 100
percentage_kid_tickets = kid_tickets / total_sold_tickets * 100
print(f'Total tickets: {total_sold_tickets}')
print(f'{percentage_student_tickets:.2f}% student tickets.')
print(f'{percentage_standard_tickets:.2f}% standard tickets.')
print(f'{percentage_kid_tickets:.2f}% kids tickets.')