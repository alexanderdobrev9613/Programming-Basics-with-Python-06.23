#user input
group_members = int(input())
nights = int(input())
cards = int(input())
tickets = int(input())

#logic

total_nights = (20 * nights) * group_members
total_cards = (1.6 * cards) * group_members
total_tickets = (6 * tickets) * group_members
total_nct = total_cards + total_tickets + total_nights
unexpected_expense = total_nct * 0.25
end_total = total_nct + unexpected_expense

#print output
print(f'{end_total:.2f}')