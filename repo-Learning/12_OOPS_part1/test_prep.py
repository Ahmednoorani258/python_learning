# class Car:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
        
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
#     def start(self):
#         print(f"{self.brand} {self.model} has started.")
        
#     def stop(self):
#         print(f"{self.brand} {self.model} has stopped.")
        
#     def __del__(self):
#         print(f"{self.brand} {self.model} has been destroyed.")
        
# car1 = Car("Toyota", "Camry")
# car2 = Car("Honda", "Civic")

# car1.start()
# car2.start()

# car1.stop()
# car2.stop()

# del car1
# del car2
        
        

# Class Attrs & Instance Attrs
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (instance attributes)
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Method to display dog details
    def display(self):
        print(f"{self.name} is {self.age} years old and is a {self.species}.")

# Create instances of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Access class attribute
print(f"Dog species: {Dog.species}")  # Output: Dog species: Canis familiaris
print(f"Buddy's species: {dog1.species}")  # Output: Buddy's species: Canis familiaris
print(f"Max's species: {dog2.species}")    # Output: Max's species: Canis familiaris

# Access instance attributes
print(f"Buddy's name: {dog1.name}")  # Output: Buddy's name: Buddy
print(f"Max's age: {dog2.age}")       # Output: Max's age: 3

# Modify class attribute (affects all instances)
Dog.species = "Canis lupus"
print(f"Buddy's species after modification: {dog1.species}")  # Output: Buddy's species after modification: Canis lupus
print(f"Max's species after modification: {dog2.species}")    # Output: Max's species after modification: Canis lupus

# Modify class attribute through an instance (creates a new instance attribute)
dog1.species = "Canis aureus"
print(f"Buddy's species after shadowing: {dog1.species}")  # Output: Buddy's species after shadowing: Canis aureus
print(f"Max's species remains: {dog2.species}")            # Output: Max's species remains: Canis lupus

# Inspect attributes using __dict__
print(f"Dog class attributes: {Dog.__dict__}")
print(f"dog1 instance attributes: {dog1.__dict__}")
print(f"dog2 instance attributes: {dog2.__dict__}")