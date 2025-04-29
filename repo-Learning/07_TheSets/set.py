
# my_set: set = {123, 452, 5, 6}
# my_set2: set = set([123, 452, 5, 6])
# unknown: set = {} # set or dectionary
# empty_set: set = set()

# print("my_set            = ", my_set)
# print("my_set2           = ", my_set2)
# print("type(my_set)      = ", type(my_set))
# print("type(my_set2)     = ", type(my_set2))
# print("type(unknown)     = ", type(unknown))
# print("type(empty_set)   = ", type(empty_set))
# print("my_set == my_set2 = ", my_set == my_set2)



# # my_set = {[123, 452, 5, 6]} # TypeError: unhashable type: 'list'
# # print(my_set) # TypeError: unhashable type: 'list'
# set3 : set = {1,2,3,4,5,6} 

# # try:
# #     set3[0] = 100 # TypeError: 'set' object does not support item assignment
# # except TypeError as e:
# #     print(e)

# set3.add(100)
# print(set3) # {1, 2, 3, 4, 5, 6, 100}
# set3.update({200, 300})
# print(set3) # {1, 2, 3, 4, 5, 6, 100, 200, 300}
# set3.discard(200)
# print(set3) #
# set3.remove(100)
# print(set3) # {1, 2, 3, 4, 5, 6, 300}
# set3.discard(100) # No error
# print(set3) # {1, 2, 3, 4, 5, 6, 300}       
# # set3.remove(100) # KeyError: 100 not found

# set3.difference_update({1,2,3})
# print(set3) # {4, 5, 6, 300}

     
# #When you call `my_set.pop()`, it removes and returns an arbitrary element from the set.
# #Since sets are unordered data structures, the element that is removed and returned is not predictable.
# set3.pop()
# print("Before pop() = ", set3)




# my_set:  set = {1,2,3, "Hello! World", 4,5,6}
# my_set2: set = {1,2,3, "Hello! World", 8,9}
# my_set3: set = {1,2,3, "Hello! World", 77}

# print("difference()           = ", my_set.difference(my_set2, my_set3)) #Returns a set containing the difference between two or more sets
# print("intersection()         = ", my_set.intersection(my_set2, my_set3))#Return a set that contains the items that exist in both set
# print("union()                = ", my_set.union(my_set2, my_set3))#Return a set that contains all items from both sets, duplicates are excluded:
# print("symmetric_difference() = ", my_set.symmetric_difference(my_set2))#One argument only, #Return a set that contains only unique items from both sets

# #my_set = {55,66}

# print("isdisjoint()           = ", my_set.isdisjoint(my_set2))#Return True if no items in set x is present in set y

# my_set2 = {1,2,3, "Hello! World"}
# print("issuperset()           = ", my_set.issuperset(my_set2))#Return True if all items in set x are present in set y
# print("issubset()             = ", my_set2.issubset(my_set))
     
     
# prompt: generate examples of all the method of set

# Example usage of set methods

# Initialize two sets for demonstration
set1: set = {1, 2, 3, 4, 5}
set2: set = {4, 5, 6, 7, 8}

# 1. add(): Adds an element to the set.
set1.add(6)
print(f"add(6): {set1}")  # Output: {1, 2, 3, 4, 5, 6}

# 2. clear(): Removes all elements from the set.
set_copy: set = set1.copy()
set_copy.clear()
print(f"clear(): {set_copy}")  # Output: set()

# 3. copy(): Returns a copy of the set.
set_copy: set = set1.copy()
print(f"copy(): {set_copy}")  # Output: {1, 2, 3, 4, 5, 6}

# 4. difference(): Returns a set containing the difference between two or more sets.
difference_set: set = set1.difference(set2)
print(f"difference(): {difference_set}")  # Output: {1, 2, 3}

# 5. difference_update(): Removes the items in this set that are also included in another, specified set.
set1.difference_update(set2)
print(f"difference_update(): {set1}")  # Output: {1, 2, 3}
set1: set = {1, 2, 3, 4, 5,6} #reset set1

# 6. discard(): Remove the specified item.
set1.discard(6)
print(f"discard(6): {set1}")  # Output: {1, 2, 3, 4, 5}

# 7. intersection(): Returns a set, that is the intersection of two other sets.
intersection_set: set = set1.intersection(set2)
print(f"intersection(): {intersection_set}")  # Output: {4, 5}

# 8. intersection_update(): Removes the items in this set that are not present in other, specified set(s)
set1.intersection_update(set2)
print(f"intersection_update(): {set1}") # Output: {4, 5}
set1 = {1, 2, 3, 4, 5,6} #reset set1

# 9. isdisjoint(): Returns whether two sets have a intersection or not.
print(f"isdisjoint(): {set1.isdisjoint(set2)}")  # Output: False
print(f"isdisjoint(): {set1.isdisjoint({9,10})}") # Output: True

# 10. issubset(): Returns whether another set contains this set or not.
print(f"issubset(): {set1.issubset(set2)}")  # Output: False
print(f"issubset(): {{1,2}}.issubset({set1})")  # Output: True
print(f"issubset(): {{1,2}}.issubset({{1,2}})")  # Output: True


# 11. issuperset(): Returns whether this set contains another set or not.
print(f"issuperset(): {set1.issuperset(set2)}")  # Output: False
print(f"issuperset(): {set1.issuperset({1,2})}")  # Output: True
print(f"issuperset(): {{1,2}}.issuperset({{1,2}})")  # Output: True

# 12. pop(): Removes a random element from the set.
removed_element: int = set1.pop()
print(f"pop(): {removed_element}")  # Output: (random element)
print(f"set after pop(): {set1}")  # Output: (set without removed_element)
set1.add(removed_element)#put back the element for others test

# 13. remove(): Removes the specified element. Raises an error if the element is not present.
set1.remove(1)
print(f"remove(1): {set1}")  # Output: {2, 3, 4, 5,6}
set1.add(1)#put back the element for others test

# 14. symmetric_difference(): Returns a set with the symmetric differences of two sets.
symmetric_difference_set: set = set1.symmetric_difference(set2)
print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: {1, 2, 3, 6, 7, 8}

# 15. symmetric_difference_update(): Inserts the symmetric differences from this set and another
set1.symmetric_difference_update(set2)
print(f"symmetric_difference_update(): {set1}")  # Output: {1, 2, 3, 6, 7, 8}
set1 = {1, 2, 3, 4, 5,6} #reset set1

# 16. union(): Returns a set containing the union of sets.
union_set = set1.union(set2)
print(f"union(): {union_set}")  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# 17. update(): Update the set with the union of this set and others
set1.update(set2)
print(f"update(): {set1}") # Output: {1, 2, 3, 4, 5, 6, 7, 8}