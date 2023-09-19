#User input
count = int(input())
rating_end = 0
possible_sales = 1
sales_done = 0

#logic
for i in range(count):
    model = input()
    rating = int(model[2])
    possible_sales = int(model[0] + model[1])
    if rating == 2:
        rating_end += 2
        sales_done += 0
    elif rating == 3:
        rating_end += 3
        sales_done += possible_sales / 2
    elif rating == 4:
        rating_end += 4
        sales_done += possible_sales * 0.7
    elif rating == 5:
        rating_end += 5
        sales_done += possible_sales * 0.85
    elif rating == 6:
        rating_end += 6
        sales_done += possible_sales


avg = rating_end / count
#print output
print(f'{sales_done:.2f}')
print(f'{avg:.2f}')