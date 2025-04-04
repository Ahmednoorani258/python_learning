# Python Typing & Dataclasses: Instance, Class, and Static Members
# This tutorial shows how to properly type instance variables/methods, class variables/methods, and static variables/methods using Python's dataclasses and typing modules.

# Key Points Explained
# Instance Members
# Variables: Defined directly in class with type hints (handled by @dataclass)
# Methods: First parameter is self, can access both instance and class data
# Default values: Use field() for mutable defaults to avoid shared state issues
# Class Members
# Variables: Annotated with ClassVar to indicate they belong to the class
# Final variables: Use ClassVar[Final] for constants that shouldn't change
# Methods: Decorated with @classmethod, first parameter is cls
# Static Members
# Variables: In dataclasses, these become instance variables with defaults
# Methods: Decorated with @staticmethod, no access to self or cls
# When to Use Each
# Instance members: For data/behavior specific to each object
# Class members: For data/behavior shared by all instances
# Static members: For utility functions that don't need instance/class access
# Instance Variables and Methods
# Instance variables are attributes that are unique to each instance of a class. Instance methods are functions that belong to an instance of a class.

# Instance Variables:
# Definition: These variables are specific to each instance (object) of the class.

# Scope: They are created and assigned when an object is instantiated, and they hold data specific to that object.

# Access: Accessed through an instance of the class using self.

# Instance Methods:
# Definition: These are the regular methods in a class that operate on instance variables.

# Scope: They work on a specific instance (object) of the class and can modify or retrieve instance variables using self.

# Access: Accessed through an instance of the class..

from dataclasses import dataclass
from typing import Optional, ClassVar, Final

from dataclasses import dataclass
from typing import Optional


# Instance Variables and Methods
# Instance variables are attributes that are unique to each instance of a class. Instance methods are functions that belong to an instance of a class.

# Instance Variables:
# Definition: These variables are specific to each instance (object) of the class.

# Scope: They are created and assigned when an object is instantiated, and they hold data specific to that object.

# Access: Accessed through an instance of the class using self.

# Instance Methods:
# Definition: These are the regular methods in a class that operate on instance variables.

# Scope: They work on a specific instance (object) of the class and can modify or retrieve instance variables using self.

# Access: Accessed through an instance of the class.
@dataclass
class Person:
    """A person with a name and age."""
    name: str
    age: int
    occupation: Optional[str] = None

    def greet(self) -> None:
        """Print a greeting message."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of Person
person = Person("John Doe", 30, "Software Engineer")
print(person)  # Person(name='John Doe', age=30, occupation='Software Engineer')
person.greet()  # Hello, my name is John Doe and I am 30 years old.



# Class Variables and Methods
# Class variables are attributes that are shared by all instances of a class. Class methods are functions that belong to a class.

# Class Variables:
# Definition: These variables are shared by all instances of the class.

# Scope: They belong to the class itself, not to any particular instance.

# Access: Accessed using the class name or via an instance, but modifying it via instances will change the variable for that specific instance, not globally.

# Class Methods:
# Definition: These methods work on the class itself rather than on a specific instance. They can modify or access class variables.

# Scope: Defined using the @classmethod decorator. They take cls as the first argument, representing the class.

# Access: Accessed using the class name or an in
@dataclass
class Person:
    """A person with a name and age."""
    name: str
    age: int
    occupation: str = "Unknown"
    species: ClassVar[str] = "Homo sapiens"

    # Final class variable (shouldn't be modified)
    #MAX_AGE: ClassVar[Final[int]] = 70

    @classmethod
    def get_species(cls) -> str:
        """Return the species of the person."""
        return cls.species

# Create an instance of Person
john = Person("John Doe", 30, "Software Engineer")
alex = Person("Alex", 25, "Accountant")

print(john.get_species())
print(alex.get_species())

Person.species = "New Species"

print(john.get_species())
print(alex.get_species())


# Static Variables and Methods
# Static variables are attributes that are shared by all instances of a class, but are not instance-specific. Static methods are functions that belong to a class, but do not have access to the class or instance.

# Static Variables:
# Definition: Static variables are variables that don't depend on the instance or class. In Python, we don’t typically use static variables, but they can be simulated using class variables or just constants.

# Scope: They are often used as constants or utility values that don’t change. They can be accessed without an instance or class.

# Static Methods:
# Definition: Static methods are utility methods that don’t need to access or modify instance or class-level data.

# Scope: Defined using the @staticmethod decorator. They do not take self or cls as parameters and are independent of both instance and class state.

# Access: Accessed directly through the class or an instance, but typically don't interact with instance or class variables.

from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    """A person with a name and age."""
    name: str
    age: int
    occupation: Optional[str] = None

    VERSION: Final[str] = '1.0.0'

    @staticmethod
    def get_version() -> str:
        """Get the Person class version"""
        return Person.VERSION

# Create an instance of Person
person = Person("John Doe", 30, "Software Engineer")
print(person.get_version())  # 1.0


# Create instances of Person
person1 = Person("John Doe", 30, "Software Engineer")
person2 = Person("Jane Doe", 25, "Doctor")

print(Person.get_version())  # 2






from typing import Any
import random

def print_value(value: Any) -> None:
    print("print_value = ", type(value), " : ", value)

print_value(123)  # prints: 123
print_value("hello")  # prints: hello

def get_value() -> Any:
    data_list: list = [1, "name", 2.0, True, {"key": "value"}]
    random_index: int = random.randint(0, len(data_list) - 1)
    return data_list[random_index]


value = get_value()
print("get_value   = ", type(value), " : ", value)



# Named Tuple Vs Data Class
from typing import NamedTuple
from dataclasses import dataclass

# NamedTuple (immutable)
class PointNT(NamedTuple):
    x: float
    y: float

# Dataclass (mutable)
@dataclass
class PointDC:
    x: float
    y: float

pnt: PointNT = PointNT(1, 2)
pdc: PointDC = PointDC(1, 2)

print(pdc)
pdc.x = 5 # ✅ mutable
print(pdc)

#pnt.x = 3 # ❌ immutable, uncomment to see error


# ______________________________________________________________________________________
# ______________________________________________________________________________________
# Advanced Features
# ______________________________________________________________________________________
# ______________________________________________________________________________________

# 1. Field Customization
from dataclasses import field

@dataclass
class InventoryItem:
    name: str
    price: float = field(default=0.0)
    tags: list[str] = field(default_factory=list)

print(InventoryItem("Apple"))


# 2. Ordering (order=True)

@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("Alice", 25)
bob = Person("Bob", 30)
print(alice < bob)  # Compares age


# 3. Inheritance

from dataclasses import dataclass

@dataclass
class Base:
    x: int

@dataclass
class Child(Base):
    y: int

    def print_x(self):
        """Print the value of x from the Base class."""
        print(self.x)  # Access x through self

# Create an instance of Child and call print_x
child_instance = Child(x=10, y=20)
print(child_instance)  # Child(x=10, y=20)
child_instance.print_x()  # Output: 10




# Real-World Example: API Response


from dataclasses import dataclass
from typing import Optional

@dataclass
class APIResponse:
    success: bool
    data: Optional[dict] = None
    error: Optional[str] = None

response = APIResponse(
    success=True,
    data={"user_id": 123}
)

print(response)


# Let's play with hashing

# prompt: create person object an use it in dict

from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Person:
    name: str
    age: int
    _ssn: str = field(repr=False)  # _ssn will not appear in __repr__

# Create Person objects
person1 = Person("Alice", 30, _ssn="123-45-6789")
person2 = Person("Bob", 25, _ssn="333-44-6666")

print("person1 = ", person1) # _ssn will not print in __repr__
print("person2 = ", person2) # _ssn will not print in __repr__

# Use Person objects in a dictionary
person_dict = {person1: "Alice's data", person2: "Bob's data"}

# Access data using Person objects as keys
print(person_dict[person1])  # Output: Alice's data
print(person_dict[person2])  # Output: Bob's data

print(person1.__hash__())

# Uncomment below code to see error
# person1.age = 40 #❌ it change the hash value
# print(person1.__hash__())
# print(person_dict[person1])  # Output: Bob's data

"""
The unsafe_hash=True argument in Python's @dataclass decorator is considered "unsafe" because it generates a hash method (hash) that relies on the mutable fields of the dataclass.

Here's a breakdown of why this is problematic:

@dataclass(unsafe_hash=True) generates a hash relying on mutable fields.

Mutable fields changing after hashing alter the object's hash.

This violates the requirement for constant hash values in dictionaries/sets.

Using such objects as dictionary keys leads to lookup failures.

"Unsafe" warns of potential errors due to mutability's impact.

It's safe only if mutable fields never change after creation.

frozen=True makes all fields immutable, ensuring safe hashing.

Manually defining __hash__ with immutable fields is another safe option.

Avoid unsafe_hash if using dataclass as dictionary keys with mutable data.

It prioritizes convenience over safety, requiring careful usage.

Performance Considerations
Slightly slower than NamedTuple due to mutability overhead
Still faster than manual class implementations
Memory usage is higher than NamedTuple
Key Takeaways
Reduces Boilerplate - Automatic __init__, __repr__, etc.
Type-Safe - Requires type hints
Flexible - Defaults, immutability, post-init processing
Pythonic - Cleaner than manual classes or NamedTuples
Great for Data Containers - Perfect for configs, DTOs, simple models
Dataclasses make Python more maintainable while keeping it clean and readable. They're now the recommended way to create data-oriented classes in modern Python. 🚀

"""