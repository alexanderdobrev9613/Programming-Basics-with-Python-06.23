
#logic
total = 0

while True:
     user_input = input() #ne e int ili float zashtoto ima i string vuv vhodovete
     if user_input == 'NoMoreMoney':
         break
     money = float(user_input) #shtom nqma da e string kato gornoto, vkarvame nova promenliva koqto veche e float/int ot inputa w cikula
     if money < 0: #ako vkarame otricatelno chislo
         print('Invalid operation!')
         break
     total += money
     print(f'Increase: {money:.2f}')


#print output
print(f'Total: {total:.2f}')