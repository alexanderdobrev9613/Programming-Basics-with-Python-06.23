#user input

end_sum = int(input())
current_payment = input()
total_payments_sum = 0
payments_count = 0
card_payments_count = 0
cash_payments_count = 0
card_sum = 0
cash_sum = 0
#sum of all cash payments / their count


#logic
while current_payment != 'End':
    current_payment = int(current_payment)
    if payments_count % 2 == 0:
        method = 'cash'
        if current_payment <= 100:
            payments_count += 1
            cash_payments_count += 1
            cash_sum += current_payment
            total_payments_sum += current_payment
            print('Product sold!')
        else:
            print("Error in transaction!")
    else:
        method = 'card'
        if current_payment >= 10:
            payments_count += 1
            card_payments_count += 1
            card_sum += current_payment
            total_payments_sum += current_payment
            print('Product sold!')
        else:
            print("Error in transaction!")
    if total_payments_sum >= end_sum:
        average_CS = cash_sum / cash_payments_count
        average_CC = card_sum / card_payments_count
        print(f"Average CS: {average_CS:.2f}")
        print(f"Average CC: {average_CC:.2f}")
        break
    current_payment = input()

#print
if current_payment == 'End':
    print('Failed to collect required money for charity.')