
#  “PYTHON OPRETORS”

# Python Operators
# 1. Arithmetic Operators

print(""" 
      Arithmetic Operators
      """)

# These operators are used to perform basic mathematical operations.
# •	Addition (+): Adds two values.
# Example: a + b (if a = 5 and b = 3, then a + b = 8)

a = 5
b = 3

print(f"Addition: {a} + {b} = {a + b}")

# •	Subtraction (-): Subtracts one value from another.
# Example: a - b (if a = 5 and b = 3, then a - b = 2)

print(f"Subtraction: {a} - {b} = {a - b}")

# •	Multiplication (*): Multiplies two values.
# Example: a * b (if a = 5 and b = 3, then a * b = 15)

print(f"Multiplication: {a} * {b} = {a * b}")

# •	Division (/): Divides one value by another, returns a float.
# Example: a / b (if a = 5 and b = 3, then a / b = 1.6667)

print(f"Division: {a} / {b} = {a / b}")

# •	Floor Division (//): Divides and returns the integer part of the result.
# Example: a // b (if a = 5 and b = 3, then a // b = 1)

print(f"Floor Division: {a} // {b} = {a // b}")

# •	Modulus (%): Returns the remainder of the division.
# Example: a % b (if a = 5 and b = 3, then a % b = 2)

print(f"Modulus: {a} % {b} = {a % b}")

# •	Exponent (**): Raises one value to the power of another.
# Example: a ** b (if a = 5 and b = 3, then a ** b = 125)

print(f"Exponent: {a} ** {b} = {a ** b}")
# ________________________________________
# 2. Comparison Operators
print(""" 
      Comparison Operators
      """)
# These operators compare two values and return True or False.
# •	Equal to (==): Checks if two values are equal.

print(f"Equal to: {a} == {b} = {a == b}")

# Example: a == b (returns False if a = 5 and b = 3)
# •	Not equal to (!=): Checks if two values are not equal.

print(f"Not Equal to: {a} != {b} = {a != b}")

# Example: a != b (returns True if a = 5 and b = 3)
# •	Greater than (>): Checks if one value is greater than another.

print(f"Greater Than: {a} > {b} = {a > b}")

# Example: a > b (returns True if a = 5 and b = 3)
# •	Less than (<): Checks if one value is less than another.

print(f"Less Than: {a} < {b} = {a < b}")

# Example: a < b (returns False if a = 5 and b = 3)
# •	Greater than or equal to (>=): Checks if one value is greater than or equal to another.
# Example: a >= b (returns True if a = 5 and b = 3)

print(f"Greater than or equal to: {a} >= {b} = {a >= b}")

# •	Less than or equal to (<=): Checks if one value is less than or equal to another.
# Example: a <= b (returns False if a = 5 and b = 3)


print(f"Less than or equal to: {a} <= {b} = {a <= b}")
# ________________________________________
# 3. Assignment Operators

print(""" 
      Assignment Operators
      """)

# These operators assign values to variables and can also perform operations during assignment.
# •	Assign (=): Assigns the value on the right to the variable on the left.
# Example: a = 10


# •	Add and assign (+=): Adds the right value to the left and assigns the result to the left.
# Example: a += 5 (if a = 10, then a = 15)
a+= 10
print(f"Add and assign: a += {10} = {a }")
# •	Subtract and assign (-=): Subtracts the right value from the left and assigns the result to the left.
# Example: a -= 5 (if a = 10, then a = 5)
a -= 10
print(f"Subtract and assign: a -= {10} = {a }")

# •	Multiply and assign (*=): Multiplies the left value by the right and assigns the result.
# Example: a *= 5 (if a = 10, then a = 50)

a *= 10
print(f"Multiply and assign: a *= {10} = {a }")

# •	Divide and assign (/=): Divides the left value by the right and assigns the result.
# Example: a /= 5 (if a = 10, then a = 2)

a /= 10
print(f"Multiply and assign: a /= {10} = {a }")
# ________________________________________
# 4. Logical Operators

print(""" 
      Logical Operators
      """)
# These operators are used to combine conditional statements.
# •	AND (and): Returns True if both conditions are true.
# Example: x > 5 and x < 10 (returns True if x = 7)

x = 8
y = 5

print(f"And: x  > 5 and x < 10 = {x  > 5 and x < 10}")

# •	OR (or): Returns True if at least one condition is true.
# Example: x > 5 or x < 3 (returns True if x = 7)
print(f"OR: x  > 5 or x < 3 = {x  > 5 or x < 3}")
# •	NOT (not): Reverses the result of a condition.
# Example: not(x > 5) (returns False if x = 7)
print(f"not: x  > 5  = {not(x  > 5) }")
# ________________________________________
# 5. Membership Operators
print(""" 
      Membership Operators
      """)
my_list = [1, 2, 3, 4, 5]
# These operators are used to test if a sequence contains a certain value.
# •	in: Returns True if the value is found in the sequence.
# Example: x in list (returns True if x is in list)
print(f"in Operator: 3 in my_list = {3 in my_list}")

# •	not in: Returns True if the value is not found in the sequence.
# Example: x not in list (returns True if x is not in list)
print(f"not in Operator: 10 not in my_list = {10 not in my_list}")
# ________________________________________
# 6. Identity Operators
print(""" 
      Identity Operators
      """)

x = [1, 2, 3]
y = x  # y points to the same object as x
z = [1, 2, 3]

# These operators compare objects to see if they are the same object in memory.
# •	is: Returns True if both variables point to the same object.
# Example: x is y (returns True if x and y point to the same object)

print(f"is Operator: x is y = {x is y}")
# •	is not: Returns True if the variables point to different objects.
# Example: x is not y (returns True if x and y point to different objects)
print(f"is not Operator: x is not z = {x is not z}")


