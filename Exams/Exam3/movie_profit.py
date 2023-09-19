#user input
movie_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
percentage_for_cinema = int(input())


#logic
total_price = number_of_tickets * ticket_price * number_of_days
total_income = total_price - ((percentage_for_cinema / 100) * total_price)
print(f'The profit from the movie {movie_name} is {total_income:.2f} lv.')

#Print output
