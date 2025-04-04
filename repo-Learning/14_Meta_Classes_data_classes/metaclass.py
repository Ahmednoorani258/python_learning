# # Meta classes

# # Metaclasses are like "classes of classes"—they define how classes themselves behave, just like classes define how instances behave.

# # Key Idea:
# # Classes are instances of metaclasses (just like objects are instances of classes).
# # By default, most classes use type as their metaclass.



# Dog = type("Dog",(),{})
# print(Dog)  # <class '__main__.Dog'>

# class Dog:
#     pass
# print(Dog)  # <class '__main__.Dog'>



# class MyMeta(type):
#     def __new__(cls, name, bases, attrs):
#         print(f"Creating class {name} with MyMeta")
#         return super().__new__(cls, name, bases, attrs)
    
    
# class Cat(metaclass=MyMeta):
#     pass

# # Output:
# # Creating class Cat with MyMeta
# # <class '__main__.Cat'>
# print(Cat)  # <class '__main__.Cat'>


# # _________________________________________
# # _________________________________________
# 3. Real-World Example: Enforce Class Rules
# Let’s force all subclasses to have a say_hello() method & class name must start with 'A':
# # _________________________________________
# # _________________________________________


# class EnforceHelloMeta(type):
#     def __new__(cls, name, bases, attrs):
#         if 'say_hello' not in attrs:
#             raise TypeError(f"{name} must implement say_hello() method")
#         if not name.startswith('A'):
#             raise TypeError(f"{name} must start with 'A'")
        
#         return super().__new__(cls, name, bases, attrs)
    
# class Animal(metaclass=EnforceHelloMeta):
#     def say_hello(self):
#         print("Hello from Animal")
        
# # class Dog(Animal):
# #     def say_hello(self):
# #         pass
    
# # class Cat(Animal):
# #     def say_hello(self):
# #         print("Meow!")
        
        
# animal = Animal()
# animal.say_hello()  # Hello from Animal
# # dog = Dog()
# # dog.say_hello()  # TypeError: Dog must implement say_hello() method
# # cat = Cat()
# # cat.say_hello()  # Meow!



# Example: Singleton Metaclass (ensures only 1 instance exists)
# class SingletonMeta(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]

# class Database(metaclass=SingletonMeta):
#     pass

# db1: Database = Database()
# db2: Database = Database()
# print(db1 is db2)  # True (same instance!)



# 4. Metaclass vs. Class Decorator
# Feature	        Metaclass	        Class Decorator	
# When it runs	    Class creation	    After class creation	
# Use case	        Deep class control	Simpler modifications	
# Example	        Enforce methods	    Add logging


# Final Verdict 🏆
# Metaclasses = "Class factories".
# Use them sparingly (only when absolutely needed).
# Most devs never write one—but understanding them helps debug big frameworks!

