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


