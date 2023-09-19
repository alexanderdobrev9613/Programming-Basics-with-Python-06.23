#user input
username = input()
password = input()
curr_password = 0

#logic
while True:
    curr_password = input()
    if curr_password == password:
        print(f'Welcome {username}!')
        break




#print output
