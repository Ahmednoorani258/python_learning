# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower

#     def start(self):
#         return "Engine started"

# class Wheel:
#     def __init__(self, size):
#         self.size = size

#     def rotate(self):
#         return f"Wheel of size {self.size} is rotating"

# class Car:
#     def __init__(self, make, horsepower, wheel_sizes):
#         self.make = make
#         self.engine = Engine(horsepower)  # Composition
#         self.wheels = [Wheel(size) for size in wheel_sizes]  # Composition

#     def drive(self):
#         return f"{self.make}: {self.engine.start()}, {[wheel.rotate() for wheel in self.wheels]}"

# class Driver:
#     def __init__(self, name):
#         self.name = name

#     def drive(self):
#         return f"{self.name} is driving"

# class Race:
#     def __init__(self, name):
#         self.name = name
#         self.cars = []  # Aggregation
#         self.drivers = []  # Aggregation

#     def add_car(self, car):
#         self.cars.append(car)

#     def add_driver(self, driver):
#         self.drivers.append(driver)

#     def start_race(self):
#         return [car.drive() for car in self.cars]

# # Testing
# car1 = Car("Toyota", 200, [17, 17, 17, 17])
# driver1 = Driver("Ali")
# race = Race("Grand Prix")
# race.add_car(car1)
# race.add_driver(driver1)
# print(race.start_race())  # ['Toyota: Engine started, [...]']



# class ValidationError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

# class User:
#     def __init__(self, username):
#         self._username = None
#         self.set_username(username)

#     def set_username(self, username):
#         try:
#             if not username or len(username) < 3:
#                 raise ValidationError("Username must be at least 3 characters long")
#             self._username = username
#         except ValidationError as e:
#             print(f"Validation failed: {e}")

#     def __str__(self):
#         return f"User: {self._username}"

# class UserManager:
#     def __init__(self):
#         self.users = []

#     def add_user(self, username):
#         user = User(username)
#         if user._username:  # Only add if username is valid
#             self.users.append(user)
#         return user

# # Testing
# manager = UserManager()
# user1 = manager.add_user("Ali")  # User created
# user2 = manager.add_user("ab")   # Validation failed: Username must be at least 3 characters long
# print(user1)  # User: Ali
# print(user2)  # User: None


# class Car():
#     pass

# print(type(int))
# print(type(Car))


