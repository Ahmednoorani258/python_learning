import string

# in this we write a function logic with copilot

def money_made(num_shares, purchase_share_price, current_share_price):
    """
 num_shares is the number of shares of a stock that we purchased.
 purchase_share_price is the price of each of those shares.
 current_share_price is the current share price.
 Return the amount of money we have earned on the stock.
 """
    return num_shares * (current_share_price - purchase_share_price)


# print(money_made(100, 20, 30))

def is_strong_password(password):
 """
 A strong password has at least one uppercase character,
 at least one number, and at least one special symbol.
 Return True if the password is a strong password, False if not.
 """
 return any(char.isupper() for char in password) and \
 any(char.isdigit() for char in password) and \
 any(not char.isalnum() for char in password)

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
    """keep asking the user for a strong password until its  a strong password  and returns that strong pass word
    """
    while True:
        password = input("Enter a strong password: ")
        if is_strong_password(password):
            return password
        
# get_strong_password()
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


# best_word(["hello", "world"])

def funct1():
 print("there")
 funct2()
 print("friend")
 funct3()
 print("")
def funct2():
 print("my")
def funct3():
 print(".")
def funct4():
 print("well")
print("Hi") #1
funct1()
print("I'm")
funct4()
funct3()
print("")
print("Bye.")


"""
Write a function that takes two inputs: the original price of an item and a discount percentage. The function should calculate and return the final price after applying the discount. Ensure the function handles cases where the discount is 0% or 100%.
"""

def calculate_discount(original_price, discount_percentage):
    if discount_percentage == 0:
        return original_price
    elif discount_percentage == 100:
        return 0
    else:
        discount_amount = original_price * (discount_percentage / 100)
        return original_price - discount_amount