#User input
Vspace = int(input())
P1 = int(input()) #debit_1st_pipe_per_hour
P2 = int(input()) #debit_2nd_pipe_per_hour
H = float(input()) #hours_worker_gone_

#Logic
total_P1 = P1 * H
total_P2 = P2 * H

total_capacity_taken = total_P2 + total_P1
total_capacity_taken_percentage = (total_capacity_taken / Vspace) * 100

P1_percentage = (total_P1 / total_capacity_taken) * 100
P2_percentage = (total_P2 / total_capacity_taken) * 100

extra_water = abs(Vspace - total_capacity_taken)

if Vspace >= total_capacity_taken:
    print(f'The pool is {total_capacity_taken_percentage:.2f}% full. Pipe 1: {P1_percentage:.2f}%. Pipe 2: {P2_percentage:.2f}%.')
else:
    print(f'For {H:.2f} hours the pool overflows with {extra_water:.2f} liters.')

#print output
