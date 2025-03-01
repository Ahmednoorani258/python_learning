# import math
# print(math)
# print(math.sqrt(16))
# print(int(math.sqrt(16)))
# ______________________________________________________________________________________

# from module import add
# print(add(2,3))
# ______________________________________________________________________________________

# import requests
# response = requests.get("https://www.google.com")
# print(response.status_code)

# ______________________________________________________________________________________

# # Basic Import
# import math
# print(math.pi)

# # Import with alias
# import numpy as np
# print(np.pi)

# # Import Specific Functions or Variables (from ... import ...)
# from math import sqrt, pi

# print (sqrt(16))
# print (pi)

# # 4. Import Everything (from module import *) (Not recommended for large modules)
# from math import *
# print (sqrt(16))

# ______________________________________________________________________________________

# x = 5
# def modify_value(x):
#     x = 10
#     print("Within function:", x)

# # Immutable object (integer)
# print("Original:", x)
# modify_value(x)
# print("After function:", x)

# ______________________________________________________________________________________

# * unpacking iterables

# def my_sum(*nums):
#     print(type(nums),", ", nums)
    
#     return sum(nums)

# print("Sum     = ", my_sum(1,2,3,4,5,8,5),"\n")
# print("Sum *[] = ", my_sum(*[1,2,3,4,5,8,5]), "\n") # *  unpacking list
# print("Sum *() = ", my_sum(*(1,2,3,4,5,8,5))) # *  unpacking tuple


# ______________________________________________________________________________________

# Positional-only arguments
# Those arguments that can only be specified by their position in the function call is called as Positional-only arguments. They are defined by placing a "/" in the function's parameter list after all positional-only parameters.

# Example

# In the following example, we have defined two positional-only arguments namely "x" and "y". This method should be called with positional arguments in the order in which the arguments are declared, otherwise, we will get an error.

# def posFun(x, y, /, z):
#     print(x + y + z)

# print("Evaluating positional-only arguments: ")
# posFun(1, 2, 3)

# # uncomment to see error
# # posFun(x=1, y=2, z=3)

# ______________________________________________________________________________________


# Keyword-only arguments
# Those arguments that must be specified by their name while calling the function is known as Keyword-only arguments. They are defined by placing an asterisk ("*") in the function's parameter list before any keyword-only parameters. This type of argument can only be passed to a function as a keyword argument, not a positional argument.

# def posFun(*, num1, num2, num3):
#     print(num1 * num2 * num3)

# print("Evaluating keyword-only arguments: ")
# posFun(num1=6, num2=8, num3=5)

# posFun(num3=6, num1=8, num2=5)


# TypeError: posFun() takes 0 positional arguments but 3 were given
#posFun(6, 8, 5)

# ______________________________________________________________________________________

# Arbitrary or Variable-length Arguments
# You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

# Syntax for a function with non-keyword variable arguments is this −

# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print ("Output is: ")
#    print (arg1)
#    for var in vartuple:
#       print ("*",var)
#    return

# # Now you can call printinfo function
# printinfo( 10 )
# printinfo( 70, 60, 50, 70, 90 )

# ______________________________________________________________________________________

# The Anonymous Functions
# The functions are called anonymous when they are not declared in the standard manner by using the def keyword. Instead, they are defined using the lambda keyword.

# Syntax
# The syntax of lambda functions contains only a single statement, which is as follows −

# lambda [arg1 [,arg2,.....argn]]:expression

# def add_two(x, y):
#   return x + y

# my_lambda = lambda x, y:  x + y;

# print(my_lambda(1,2))


# my_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}

# sorted_dict = dict(sorted(my_dict.items(),key=lambda x: x[1],))
# sorted_dict = dict(sorted(my_dict.items(),key=lambda x: x[1], reverse=True))

# print(sorted_dict)

# ______________________________________________________________________________________

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# def my_function(**student: dict):
#     print("\nHis last name is " + student["lname"])

#     for key,val in student.items():
#         print(key, ":", val)
    
#     print("\n")
#     print(student)
    
# my_function(fname = "Ali", lname = "Osman")

# my_function(fname = "Ali", lname = "Osman", course = "Python - 101", day="Saturday", time="1400 - 1800")

# my_dict = {"fname": "Arif", "lname": "Rozani", "course":"101 - 201", "day":"Saturday | Sunday", "role":"Student"}
# # my_function(my_dict) # uncomment to see TypeError
# my_function(**my_dict) # use ** to unpack the dictionary

# ______________________________________________________________________________________

# Generator Function
# A generator function in Python is a special type of function that allows you to iterate over a sequence of values without storing the entire sequence in memory. Instead of returning a single value using return, a generator function uses the yield keyword to produce a series of values, one at a time, on-the-fly. This makes generator functions highly memory-efficient for working with large or infinite sequences.

# Key Features of Generator Functions
# Lazy Evaluation: Values are generated only when needed, not all at once.

# Memory Efficiency: Only one value is stored in memory at a time.

# Iterable: Generator functions return a generator object, which can be iterated over using a for loop or functions like next().

# Resumable: The state of the generator function is saved between yield calls, allowing it to resume execution from where it left off.

# Syntax of a Generator Function
# A generator function is defined like a normal function but uses the yield keyword instead of return.

# def generator_function():
#     yield value
# How Generator Functions Work
# When a generator function is called, it returns a generator object without executing the function body.

# The function body executes only when the generator object is iterated over (e.g., using a for loop or next()).

# When the yield statement is encountered, the function pauses and returns the yielded value. The function’s state (e.g., local variables) is saved.

# The function resumes execution from where it left off the next time next() is called or the generator is iterated over.

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3

# # Create a generator object
# gen = simple_generator()

# print(gen, " : ", type(gen))

# # Iterate over the generator
# for value in gen:
#     print(value, " : ", type(value))
    

# # print(next(gen)) #error: StopIteration


# def infinite_sequence():
#     num = 0
#     while True:
#         yield num # Since yield pauses execution, it remembers the state and resumes from there when next() is called.
#         num += 1

# # Create a generator object
# gen = infinite_sequence() #initializes the generator.

# # Print the first 5 numbers, _ is a throw away variable
# for _ in range(5):
#     print(next(gen)) # The next time we call next(gen), execution resumes from where it left off.
    
    
# def infinite_loop(): #without yield it become infinite
#    num = 0
#    while True:
#        #yield num   # with yield it become generator without yield its a infinite loop
#        num += 1
#        print("infinite_loop() : num = ", num)

# infinite_loop()

# Generator Expressions
# Generator expressions are a concise way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets.

# Example:


# [ ]

# Generator expression
# gen = (x * x for x in range(10))
# print(type(gen))

# # Iterate over the generator
# for value in gen:
#     if value % 2 == 0:
#         print(value, " : ", type(str(value)))
#     print(value, " : ", type(value))

# ______________________________________________________________________________________

# def factorial(n):
#     # Base case
#     if n == 0:
#         return 1
#     # Recursive case
#     else:
#         print (n, factorial(n-1))
#         return n * factorial(n - 1)

# # Example usage
# print(factorial(6))  # Output: 120

# ______________________________________________________________________________________

