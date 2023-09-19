#user input
movie_name = input()
current_score = 0
max = 0
limit = 1
favorite = ''
isfound = True


#logic
while movie_name != 'STOP':
    if limit == 7:
        print('The limit is reached.')
        break
    else:
        current_score = 0
        for i in range(len(movie_name)):
            current_score += ord(movie_name[i])
            if 65 <= ord(movie_name[i]) <= 90:
                current_score -= len(movie_name)
            elif 97 <= ord(movie_name[i]) <= 122:
                current_score -= 2 * len(movie_name)
    if max <= current_score:
        max = current_score
        favorite = movie_name
    limit += 1
    movie_name = input()

#print output
print(f'The best movie for you is {favorite} with {max} ASCII sum.')