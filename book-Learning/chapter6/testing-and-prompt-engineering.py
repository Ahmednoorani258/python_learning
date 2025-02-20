# def longest_word(words):
#     '''
#     words is a list of words

#     return the word from the list with the most characters
#     if multiple words are the longest, return the first
#     such word

#     >>> longest_word(['cat', 'dog', 'bird'])
#     'bird'
#     >>> longest_word(['happy', 'birthday', 'my', 'cat'])
#     'birthday'
#     >>> longest_word(['happy'])
#     'happy'
#     >>> longest_word(['cat', 'dog', 'me'])
#     'cat'
#     >>> longest_word(['', ''])
#     ''
#     ''' 

#     longest_word = ''  # Initialize longest_word variable
#     longest_length = 0
#     for word in words:
#         if len(word) > longest_length:
#             longest_word = word
#             longest_length = len(word)
#     return longest_word


# def most_students(classroom):
#     """
#     classroom is a list of lists 
#     each "" represents a empty seat
#     each string represents a student's name

#     how many new students can be added to the classroom
    
#     >>> most_students([['S', ' ', 'S', 'S', 'S', 'S'], \ #1
#  ['S', 'S', 'S', 'S', 'S', 'S'], \
# [' ', 'S', ' ', 'S', ' ', ' ']])
#     """
    
#     max_students = 0
#     for row in classroom:
#         students = 0
#         for seat in row:
#             if seat == 'S':
#                 students += 1
#             else:
#                 students = 0
#         if students > max_students:
#             max_students = students
#     return max_students

# import doctest
# doctest.testmod(verbose=True)


def tot_pass_yds_player(input_file, player):
    """
    input_file is a string that is the name of a file
    player is the name of a player

    The file is a csv file with a header row
    Column 4 is the player's name and column
    8 is the number of passing yards for that player

    return the total number of passing yards for the player
    >>> tot_pass_yds_player('e:/CODING/08_Python/book-Learning/chapter6/test_file.csv', 'Aaron Rodgers')
    800
    >>> tot_pass_yds_player('e:/CODING/08_Python/book-Learning/chapter6/test_file.csv', 'Kerryon Johnson')
    5
    >>> tot_pass_yds_player('e:/CODING/08_Python/book-Learning/chapter6/test_file.csv', 'Leo Porter')
    0
    >>> tot_pass_yds_player('e:/CODING/08_Python/book-Learning/chapter6/test_file.csv', 'Jared Goff')
    190
    >>> tot_pass_yds_player('e:/CODING/08_Python/book-Learning/chapter6/test_file.csv', 'Dan Zingaro')
    -10
    >>> tot_pass_yds_player('e:/CODING/08_Python/book-Learning/chapter6/test_file.csv', 'Tom Brady')
    0
    """
    import csv
    
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        total = 0
        for row in reader:
            if row[3] == player:
                try:
                    total += int(row[7])
                except ValueError:
                    pass
    return total

import doctest
doctest.testmod(verbose=True)