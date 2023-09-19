#user input
dancers = int(input())
points = float(input())
season = input()
location = input()
end_prize = 0

#logic
if location == 'Bulgaria':
    end_prize += points * dancers
    if season == 'summer':
        end_prize -= end_prize * 0.05
    elif season == 'winter':
        end_prize -= end_prize * 0.08
elif location == 'Abroad':
    end_prize += (points * dancers) + (points * dancers) / 2
    if season == 'summer':
        end_prize -= end_prize * 0.1
    elif season == 'winter':
        end_prize -= end_prize * 0.15

charity = end_prize * 0.75
prize_dancer = (end_prize - charity) / dancers

#print output
print(f'Charity - {charity:.2f}')
print(f'Money per dancer - {prize_dancer:.2f}')