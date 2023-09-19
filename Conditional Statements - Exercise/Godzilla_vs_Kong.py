#user input
movie_budget = float(input())
number_of_statist = int(input())
clothing_price_per_statist = float(input())

#logic
decor = movie_budget * 0.1
total_clothing_price = clothing_price_per_statist * number_of_statist

if number_of_statist > 150:
    clothing_price_per_statist *= 0.9

total_clothing_price = clothing_price_per_statist * number_of_statist

total_movie_cost = abs((total_clothing_price + decor) - movie_budget)

if total_movie_cost > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {total_movie_cost:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {total_movie_cost:.2f} leva left.")


#print output
