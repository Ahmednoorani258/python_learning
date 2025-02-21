# def count_words(words):
#  count = 0
#  for word in words:
#     if "dan" in word.lower():
#         count += 1
#  return count
# words = ["Dan", "danger", "Leo"] #1
# print(count_words(words))


def sum_even_numbers(numbers):
 total = 0
 for number in numbers:
    if number % 2 == 0:
        total += number
 else:
    total = 0
 return total


def find_max(numbers):
 max_number = 0
 for i in range(0, len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]
 return max_number