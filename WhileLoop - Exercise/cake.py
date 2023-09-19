# user input
cake_width = int(input())
cake_length = int(input())

# logic
pieces_per_guest = input()
piece_count = cake_length * cake_width

while pieces_per_guest != 'STOP':
    pieces_per_guest = int(pieces_per_guest)
    piece_count -= pieces_per_guest
    if piece_count < 0:
        diff = abs(piece_count)
        print(f'No more cake left! You need {diff} pieces more.')
        break
    pieces_per_guest = input()

# print output
if pieces_per_guest == 'STOP':
    print(f'{piece_count} pieces are left.')