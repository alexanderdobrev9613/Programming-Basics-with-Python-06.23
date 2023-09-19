
#logic
max_number = int(input()) #zashtoto ne znaem koe e nai golqmoto toest e purvoto koeto ni vkarat

while True:
    user_input = input()
    if user_input == 'Stop':
        break
    number = int(user_input) #prevrushtame v chislo za da mojem da proverim nadolu
    if number > max_number:
        max_number = number

#print output
print(max_number)