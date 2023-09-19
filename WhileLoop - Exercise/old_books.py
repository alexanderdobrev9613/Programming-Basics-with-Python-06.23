#user input

searched_book = input()
books_counter = 0
book_is_found = False
current_book = input()

#logic

while current_book != 'No More Books':
    if current_book == searched_book:
        book_is_found = True
        break
    books_counter += 1
    current_book = input()

#print output
if book_is_found:
    print(f'You checked {books_counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {books_counter} books.')