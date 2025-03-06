# class Bakery:
#     type = "cake"  # Class variable

#     def __init__(self, flavor, price):
#         self.flavor = flavor  # Instance variable
#         self.price = price    # Instance variable

#     def update_cake_count(cls, count):
#         cls.cake_count = count

# #Accessing
# print(Bakery.type)

# cake1 = Bakery("Chocolate", 25.00)
# cake2 = Bakery("Vanilla", 22.00)

# print(cake1.flavor)
# print(cake2.price)

# #Modifying
# Bakery.type = "pastry"
# print(cake1.type)

# cake1.type = "cookie"
# print(cake1.type)
# print(cake2.type)



# # Composition
# class Engine:
#     def start(self):
#         return "Engine starting"

# class Car:
#     def __init__(self):
#         self.engine = Engine()  # Composition: Car *has-a* Engine, and owns it

#     def start(self):
#         return f"Car starting: {self.engine.start()}"

# # Aggregation
# class Department:
#     def __init__(self, name):
#         self.name = name

# class University:
#     def __init__(self, name):
#         self.name = name
#         self.departments = []  # University *has-a* Department, but doesn't own it

#     def add_department(self, department):
#         self.departments.append(department)


# # Define the classes
# class A:
#     def greet(self):
#         return "Hello from A"

# class B(A):
#     def greet(self):
#         return "Hello from B"

# class C(A):
#     def greet(self):
#         return "Hello from C"

# class D(B, C):
#     pass

# # Create an instance of D
# d = D()

# # Check the MRO of class D
# print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# # Call the greet method
# print(d.greet())  # Output: Hello from B

    #  

# # BankAccount class
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     # Method to deposit money
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive.")
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")

#     # Method to withdraw money
#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive.")
#         if self.balance < amount:
#             raise InsufficientFundsError(self.balance, amount)
#         self.balance -= amount
#         print(f"Withdrew {amount}. New balance: {self.balance}")

#     # Method to display account details
#     def display(self):
#         print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

# # Create a BankAccount instance
# account = BankAccount("Alice", 1000)

# # Deposit money
# try:
#     account.deposit(500)  # Output: Deposited 500. New balance: 1500
# except ValueError as e:
#     print(e)

# # Withdraw money
# try:
#     account.withdraw(2000)  # Raises InsufficientFundsError
# except InsufficientFundsError as e:
#     print(e)  # Output: Insufficient funds: balance is 1500, but 2000 was requested.
# except ValueError as e:
#     print(e)

# # Display account details
# account.display()  # Output: Account Holder: Alice, Balance: 1500