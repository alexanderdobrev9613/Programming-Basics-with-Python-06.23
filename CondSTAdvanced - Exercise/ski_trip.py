#user input
days = int(input())
accommodation = input()
rating = input()

nights = days - 1
price_per_night = 0


#logic
if accommodation == 'room for one person':
    price_per_night = 18
    total_price = price_per_night * nights
    if rating == 'positive':
        total_price = total_price + (total_price * 0.25)
    else:
        total_price = total_price - (total_price * 0.1)

elif accommodation == 'apartment':
    price_per_night = 25
    total_price = price_per_night * nights
    if days < 10:
        total_price = total_price - (total_price * 0.3)
        if rating == 'positive':
            total_price = total_price + (total_price * 0.25)
        else:
            total_price = total_price - (total_price * 0.1)

    elif 10 <= days <= 15:
        total_price = total_price - (total_price * 0.35)
        if rating == 'positive':
            total_price = total_price + (total_price * 0.25)
        else:
            total_price = total_price - (total_price * 0.1)

    elif days > 15:
        total_price = total_price - (total_price * 0.5)
        if rating == 'positive':
            total_price = total_price + (total_price * 0.25)
        else:
            total_price = total_price - (total_price * 0.1)

elif accommodation == 'president apartment':
    price_per_night = 35
    total_price = price_per_night * nights
    if days < 10:
        total_price = total_price - (total_price * 0.1)
        if rating == 'positive':
            total_price = total_price + (total_price * 0.25)
        else:
            total_price = total_price - (total_price * 0.1)

    elif 10 <= days <= 15:
        total_price = total_price - (total_price * 0.15)
        if rating == 'positive':
            total_price = total_price + (total_price * 0.25)
        else:
            total_price = total_price - (total_price * 0.1)

    elif days > 15:
        total_price = total_price - (total_price * 0.2)
        if rating == 'positive':
            total_price = total_price + (total_price * 0.25)
        else:
            total_price = total_price - (total_price * 0.1)


#print output

print(f'{total_price:.2f}')