# The Set Data Type
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is:

# unordered
# unchangeable
# unindexed
# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.

my_set: set = {123, 452, 5, 6}
my_set2: set = set([123, 452, 5, 6])

print("my_set            = ", my_set)
print("my_set2           = ", my_set2)
print("type(my_set)      = ", type(my_set))
print("type(my_set2)     = ", type(my_set2))
print("my_set == my_set2 = ", my_set == my_set2)