# Loops
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


def best_word(word_list):
 """
 word_list is a list of words.

 Return the word worth the most points.
 """
 best_word = ""
 best_points = 0
 for word in word_list: #1
    points = num_points(word)
 if points > best_points:
    best_word = word
 best_points = points
 return best_word

#  s='vacations'
#  for char in s:
#      print('Next Letter Is ',char)

lst = ['cat', 'dog', 'bird', 'fish']
# for animal in lst: #1
#  print('Got', animal) #2
# #  print('Hello,', animal) #2

# for animal in range(0, len(lst)): 
#  print('Got', lst[animal])

def is_strong_password(password):
 """
 A strong password has at least one uppercase character,
 at least one number, and at least one punctuation.
 Return True if the password is a strong password, False if not.
 """
 return any(char.isupper() for char in password) and \
 any(char.isdigit() for char in password) and \
 any(char in string.punctuation for char in password)


def get_strong_password():
 """
 Keep asking the user for a password until it’s a strong password,
 and return that strong password.
 """
 password = input("Enter a strong password: ")
 while not is_strong_password(password): #1
    password = input("Enter a strong password: ")
 return password

# 
# index = 0
# while index < len(lst): #1
#  print('Got', lst[index])
#  print('Hello,', lst[index])
#  index += 1 
 
 
medals = [[2, 0, 2],
[1, 2, 0],
[1, 1, 0],
[0, 1, 0],
[1, 0, 0]]

for i in range(len(medals)): 
    for j in range(len(medals[i])):
        print(i, j, medals[i][j])

