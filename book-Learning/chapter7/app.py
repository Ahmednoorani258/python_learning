def create_word_list(filename): #1
 ''' #2
 filename is the name of a file that has one English word per line.
 Return a list of the words in the file.
 '''
 file = open(filename) #3
 words = []
 for line in file: #4
    words.append(line.strip()) #5
 file.close()
 return words

def add_letter(word):
 '''
 word is a string with at least one letter.
 Return a list of all the strings that can be obtained by
 adding one letter to word.
 '''
 words = []
 for i in range(len(word) + 1): #1
    for c in 'abcdefghijklmnopqrstuvwxyz': #2
        new_word = word[:i] + c + word[i:] #3
 words.append(new_word) #4
 return words

def delete_letter(word):
 '''
 word is a string with at least one letter.
 Return a list of all the strings that can be obtained by
 deleting one letter from word.
 >>> delete_letter('carf')
 ['arf', 'crf', 'caf', 'car']
 >>> delete_letter('a')
 ['']
 '''
 words = []
 for i in range(len(word)): #1
    new_word = word[:i] + word[i + 1:] #2
 words.append(new_word) #3
 return words

def change_letter(word):
 '''
 word is a string with at least one letter.
 Return a list of all the strings that can be obtained by
 changing one letter to another letter in word.
 '''
 words = []
 for i in range(len(word)): #1
    for c in 'abcdefghijklmnopqrstuvwxyz': #2
        if c != word[i]: #3
            new_word = word[:i] + c + word[i + 1:] #4
 words.append(new_word) #5
 return words

def all_possible_words(word):
 '''
 word is a string with at least one letter.
 Return a list of all the strings that can be obtained by
 adding one letter to word, deleting one letter from word,
 or changing one letter in word.
 '''
 return add_letter(word) + delete_letter(word) + change_letter(word) #2


def all_real_words(word_list, possible_words):
 '''
 word_list is a list of English words.
 possible_words is a list of possible words.
 Return a list of words from possible_words that are in word_list.
 >>> english_words = ['scarf', 'cat', 'card', 'cafe']
 >>> possible_words = ['carfe', 'card', 'cat', 'cafe']
 >>> all_real_words(english_words, possible_words)
 ['card', 'cat', 'cafe']
 '''
 real_words = []
 for word in possible_words: #1
    if word in word_list: #2
        real_words.append(word) #3
 return real_words

def get_spelling_suggestions(word_file, possible_word):
 '''
 word_file is the name of a file that has one English word per line.
 possible_word is a string that may or may not be a real word.
 Return the list of all possible unique corrections
 for possible_word.
 '''
 word_list = create_word_list(word_file) #1
 possible_words = all_possible_words(possible_word) #2
 real_words = all_real_words(word_list, possible_words) #3
 return list(set(real_words)) #4

def spell_check(word_file):
 '''
 word_file is the name of a file that has one English word per line.
 Ask user for a word.
 Print all possible corrections for the word, one per line.
 '''
 word = input('Enter a word: ') #1
 suggestions = get_spelling_suggestions(word_file, word) #2
 for suggestion in suggestions: #3
    print(suggestion) #4

# spell_check('wordlist.txt')


def process_orders(orders):
 total_price = 0
 for order in orders:
    price = order['price']
 quantity = order['quantity']
 total_price += price * quantity
 tax = total_price * 0.08
 total_price_with_tax = total_price + tax
 report = f"Total price: ${total_price:.2f}\n"
 report += f"Tax: ${tax:.2f}\n"
 if total_price_with_tax > 100:
    discount = total_price_with_tax * 0.1
 total_price_with_tax -= discount
 report += f"Discount: ${discount:.2f}\n"
 report += f"Total price with tax: ${total_price_with_tax:.2f}\n"
 print(report)
a = {'price': 20, 'quantity': 5}
lst = [a]
process_orders(lst)

def calculate_average(numbers):
 total = sum(numbers)
 count = len(numbers)
 return total / count
def process_numbers(data):
 valid_numbers = [n for n in data if isinstance(n, int)]
 average = calculate_average(valid_numbers)
 print(f"The average of the valid numbers is: {average}")
# Test Case 1
data = [10, 20, 'a', 30, 'b', 40]
process_numbers(data)
# Test Case 2
data = ['a', 'b']
process_numbers(data)