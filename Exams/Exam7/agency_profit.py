#user input
name = input()
grownup_ticket = int(input())
kid_ticket = int(input())
grownup_ticket_price = float(input())
tax = float(input())

#logic
kid_ticket_price = grownup_ticket_price - (grownup_ticket_price * 0.7)
end_grownup = grownup_ticket_price + tax
end_kid = kid_ticket_price + tax
total_price = (end_kid * kid_ticket) + (grownup_ticket * end_grownup)
income = 0.2 * total_price

#print output
print(f'The profit of your agency from {name} tickets is {income:.2f} lv.')