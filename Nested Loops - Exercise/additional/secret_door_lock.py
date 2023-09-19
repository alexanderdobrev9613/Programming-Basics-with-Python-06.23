#user input
up_hundreds = int(input())
up_tens = int(input())
up_ones = int(input())

#logic
for first in range(1, up_hundreds + 1):
    for second in range(1, up_tens + 1):
        for third in range(1, up_ones + 1):
            if (first % 2 == 0 and third % 2 == 0) and 2 <= second <= 7:
                is_prime = True
                for i in range(2, second):
                    if second % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(f'{first} {second} {third}')


#print output