# Dataclasses in Python: A Complete Guide
# Dataclasses are a powerful Python feature introduced in Python 3.7 (via PEP 557) that automatically generate common boilerplate code for classes. They're designed to simplify class creation when the class primarily stores data.

# What is a dataclass in Python?
# A dataclass in Python is a decorator introduced in Python 3.7 that simplifies the creation of classes used primarily for storing data. A dataclass automatically adds special methods to the class, like:

# __init__: a constructor method to initialize attributes.

# __repr__: a method that provides a human-readable string representation of the object.

# __eq__: a method for comparing instances for equality based on their attributes.

# __hash__: a method that allows instances of the class to be used as dictionary keys or in sets.

# These methods are automatically generated, reducing the need for boilerplate code and making the code more concise and readable.

# Why do we need dataclass?
# In traditional Python, when we create a class to store data, we have to manually implement special methods like __init__, __repr__, __eq__, and others. This can result in repetitive and error-prone code, especially if the class is primarily used to hold data with little additional logic.

# Before dataclass, a typical Python class for holding data might look like this:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Person(name={self.name}, age={self.age})"

#     def __eq__(self, other):
#         if isinstance(other, Person):
#             return self.name == other.name and self.age == other.age
#         return False
    
# # prompt: use person class

# person: Person = Person("Alice", 30)
# print(person)  # Output: Person(name='Alice', age=30)



# # With dataclass, the code becomes much simpler:
# from dataclasses import dataclass

# @dataclass(unsafe_hash=True) # We will discuss unsafe_hash later in the tutorial
# class Person:
#     name: str
#     age: int
    
# # Same functionality in 6 lines instead of 12!

# # prompt: use person class in example showing repr eq and hash dunders

# # Example usage
# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)
# person3 = Person("Alice", 30)

# print("person1               = ", person1)  # Output using __repr__
# print("person1 == person2    = ", person1 == person2)  # Output using __eq__
# print("person1 == person3    = ", person1 == person3)  # Output using __eq__

# # Demonstrate hashing
# person_set = {person1, person2}
# print("person1 in person_set = ", person1 in person_set)  # True
# print("person3 in person_set = ", person3 in person_set)  # True (because person1 and person3 are equal)

# person_dict = {person1: "Alice's data"}
# print("person_dict[person3]  = ", person_dict[person3]) # Access using person3 (equal to person1)

# print(person1.__hash__())
# person1.age = 40
# print(person1.__hash__())
# person1.age = 30
# print(person1.__hash__())




# @dataclass
# class Point:
#     x: float  # Type hints are mandatory
#     y: float

# @dataclass
# class User:
#     username: str
#     is_active: bool = True  # Default value
    
    
# @dataclass(frozen=True)
# class Config:
#     api_key: str

# config = Config("secret")
# #config.api_key = "new"  # ❌ Error: frozen instance, uncomment to see error



# @dataclass
# class Person:
#     name: str
#     age: int

#     def __post_init__(self):
#         self.adult = self.age >= 18
#         print("Post init...")

# Person("Alice", 25)

# When to Use Dataclasses?
# ✅ DTOs (Data Transfer Objects)
# ✅ Configuration objects
# ✅ Simple domain models
# ✅ Any class storing data with little logic

# ❌ Not ideal for complex behavior-heavy classes