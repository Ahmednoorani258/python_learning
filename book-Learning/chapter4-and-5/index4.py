def num_points(word):
 """
 Each letter is worth the following points:
 a, e, i, o, u, l, n, s, t, r: 1 point
 d, g: 2 points
 b, c, m, p: 3 points
 f, h, v, w, y: 4 points
 k: 5 points
 j, x: 8 points
 q, z: 10 points
 word is a word consisting of lowercase characters.
 Return the sum of the points for the word.
 """
 return sum(1 if char in "aeioulnst" else 2 if char in "dg" else 3 if char in "bcmp" else 4 if char in "fhvwy" else 5 if char == "k" else 8 if char in "jx" else 10 for char in word)

# num_points("hello")# 8

def best_word(word_list):
 """
 word_list is a list of words.

 Return the word with the most points.
 """
 best_word = ""
 best_points = 0
 for word in word_list:
    points = num_points(word)
    if points > best_points:
        best_word = word
        best_points = points
 return best_word


# """ after selecting code run press ctrl + alt + i to explain the code by copilot """


# press Ctrl–Shift–P and type REPL, and then select Python:
# Start REPL. This should result in the situation shown in figure
# 4.5. (REPL stands for read-execute-print-loop. It’s called that
# because Python reads what you type, executes/runs it, prints
# the results back to you, and does all of this over and over in
# a loop.)

# witht he help of this we can easilt test thing in terminal

max(4,5,10)

# now we have many options to run or test this code
# 1) in terminal repl
# 2) by selecting code and press shift enter
# 3) in terminal runtime environment
# 4) by prssing atrl + alt + i to check output by copilot

def clean_number(phone_number):
 phone_number = phone_number.replace('(', '') #1
 phone_number = phone_number.replace(')', '') #2
 phone_number = phone_number.replace('-', '') #3
 return phone_number

# print(clean_number("(92)-335-3791610"))

# Whereas we use quotation marks to start and end a string,
# we use opening and closing square brackets to start and end
# a list. And, as for strings, there are many methods available
# on lists. To give you an idea of the kinds of list methods
# available and what they do, let’s explore some of these:
# >>> books = ['The Invasion', 'The Encounter', 'The Message'] #1
# >>> books
# ['The Invasion', 'The Encounter', 'The Message']
# # >>> books.append('The Predator') #2
# # >>> books
# ['The Invasion', 'The Encounter', 'The Message', 'The Predator']
# # >>> books.reverse() #3
# # >>> books
# ['The Predator', 'The Message', 'The Encounter', 'The Invasion']

books = ['The Predator', 'The Message', 'The Encounter', 'The Invasion']

print(books[0])
print(books[1])
print(books[2])
print(books[-2])
print(books[-1])
print(books[-3])

print(books[1:8])
print(books[1:2])
print(books[:4])
print(books[1:])


# f we try that on a string, though, we get an error:
# >>> title = 'The Invasion'
# >>> title[0] #1
# 'T'
# >>> title[1]
# 'h'
# >>> title[-1]
# 'n'
# >>> title[0] = 't' #2
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# #1 Looking up a char works fine.
# #2 But assigning doesn’t!
# A string is known as an immutable value, which means that
# you can’t change its characters. You can only create an
# entirely new string. By contrast, a list is known as a mutable
# value, which means that you can change it. If you get errors
# about a type not supporting item assignment, you’re likely
# trying to change a value that can’t be changed.


# Code
# Element Example Brief Description
# Functions def larger(num1, num2)
# Code feature that allows us to manage
# code complexity. Functions take in
# inputs, process those inputs, and
# possibly return an output.
# Variables age = 25
# A human-readable name that refers to a
# stored value. It can be assigned using
# the = assignment statement.
# Conditionals
# if age < 18:
# print("Can't vote")
# else: print("Can
# vote")
# Conditionals allow the code to make
# decisions. In Python, we have three
# keywords associated with conditionals:
# if, elif, and else.
# Strings name = 'Dan'
# Strings store a sequence of characters
# (text). There are many powerful
# methods available for modifying strings.
# Lists list = ['Leo', 'Dan']
# A sequence of values of any type. There
# are many powerful methods available
# for modifying lists.