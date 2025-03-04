# #  Encapsulation

# # class Car:
# #     def __init__(self, speed, color):
# #         self.__speed = speed
# #         self.color = color
    
# #     def accelerate(self):
# #         self.__speed += 10
# #         return self.__speed

# #     def getspeed(self):
# #         return self.__speed
        
        
# # car = Car(10, 'red')
# # print(car.accelerate())
# # print(car.accelerate())
# # print(car.accelerate())

# # print(car.getspeed()) #car.getspeed()

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self._engine_status = 'off'
#         self._idling_time = 0
#         self._traffic_signal = None
    
#     def drive(self):
#         if self._engine_status and self._traffic_signal == "green":
#             print(f"You are driving a {self.brand} {self.model}.")
#         elif self._traffic_signal == "red":
#             print(f"You stopped at the red light in a {self.brand} {self.model}.")
#             self._idle_stop_engine()
#         else:
#             self._start_engine()
#             print(f"You are driving a {self.brand} {self.model}.")
    
#     def stop(self):
#          if self._engine_status:
#             print(f"You stopped the {self.brand} {self.model}.")
#             self._idle_stop_engine()
#          else:
#             print(f"The {self.brand} {self.model} is already stopped.")
    
#     def set_traffic_signal(self, color):
#         self._traffic_signal = color
#         if color == "red":
#             print(f"Traffic signal turned red. You stopped in a {self.brand} {self.model}.")
#             self._idle_stop_engine()
#         elif color == "green":
#             print(f"Traffic signal turned green. You can drive your {self.brand} {self.model}.")
#             if not self._engine_status:
#                 self._start_engine()
#     def _start_engine(self):
#         self._engine_status = 'on'
#         self._idling_time = 0
#         print(f"The {self.brand} {self.model} engine is started.")
    
#     def _idle_stop_engine(self):
#         import time
#         print('Engine is idling')
        
#         for i in range(5):
#             print(f"Engine will stop in {5-i} seconds.")
#             time.sleep(1)
#             self._idling_time += 1
        
#         if self._idling_time >= 5:
#             self._engine_status = 'off'
#             print(f"The {self.brand} {self.model} engine is stopped.")
            
            
# # my_car = Car("Toyota", "Camry")
# # my_car.set_traffic_signal("green")
# # my_car.drive()
# # my_car.set_traffic_signal("red")
# # my_car.set_traffic_signal("green")
# # my_car.drive()

# class BMW(Car):
#   def __init__(self, brand, model):
#     super().__init__(brand, model)

#   def start_engine(self):
#     self._start_engine() # Car class private method is visible in child class

#   def _start_engine(self): # Overrides the parent method with the same name
#     print("BMW engine started") # Even you can override it

# bmw: BMW = BMW("BMW", "i5");
# bmw.start_engine();

# class Vehicle:
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
    
#     def drive(self):
#         print(f"Driving at {self.speed} kmph.")
        
#     def stop(self):
#         print("Stopping the vehicle.")
        
    
# class Car(Vehicle):
#     def __init__(self, color, speed):
#         super().__init__(color, speed)

# class Bike(Vehicle):
#     def __init__(self, color, speed):
#         super().__init__(color, speed)
        
        
# car = Car("red", 120)
# truck = Bike("blue", 80)

# car.drive()
# truck.drive()


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self) -> None:
#         pass

# class Dog(Animal):
#     def speak(self) -> None:
#         print(type(self), ":  Woof!")

# class Cat(Animal):
#     def speak(self) -> None:
#         print(type(self), ":  Meow!")

# def animal_sound(animal: Animal) -> None:
#     animal.speak()

# dog = Dog()
# cat = Cat()
# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!


class MagicToyCatalog:
    def __init__(self):
        self.toys = {}
        self._secret_offer = "Free plushie with any purchase!"

    def __setitem__(self, name, details):
        """Add/update toys like catalog['RoboDog'] = (49.99, 'RC dog')"""
        self.toys[name] = details

    def __getitem__(self, name):
        """Get toy details using catalog['RoboDog']"""
        return self.toys.get(name, ("Unknown", "Not in stock"))

    def __delitem__(self, name):
        """Remove items with del catalog['RoboDog']"""
        if name in self.toys:
            del self.toys[name]
            print(f"Poof! {name} vanished from the catalog!")
        else:
            raise MagicToyError(f"✨ {name} doesn't exist in our dimension")

    def __contains__(self, name):
        """Check existence with 'RoboDog' in catalog"""
        return name in self.toys

    def __len__(self):
        """Get count with len(catalog)"""
        return len(self.toys)

    def __iter__(self):
        """Iterate with for toy in catalog"""
        return iter(self.toys.items())

    def __add__(self, other):
        """Combine catalogs: mega_catalog = catalog1 + catalog2"""
        combined = MagicToyCatalog()
        combined.toys = {**self.toys, **other.toys}
        return combined

    def __str__(self):
        """User-friendly display"""
        header = "🔮 Magic Toy Catalog 🔮\n"
        items = "\n".join([f"- {name}: ${price} ({desc})"
                          for name, (price, desc) in self.toys.items()])
        return header + (items if items else "✨ Empty (for now)")

    def __repr__(self):
        """Developer representation"""
        return f"<MagicToyCatalog: {len(self)} toys>"

    def __call__(self, discount=0):
        """Activate special offers: catalog(10) for 10% off"""
        return "\n".join([f"{name}: ${price * (1 - discount/100):.2f}"
                         for name, (price, desc) in self.toys.items()])

class MagicToyError(Exception):
    pass



# Create catalogs
kids_toys = MagicToyCatalog()
collector_editions = MagicToyCatalog()

# Add items using __setitem__
kids_toys["RoboDog"] = (49.99, "Self-charging robot dog")
kids_toys["MagicKit"] = (29.95, "150 magic tricks set")
collector_editions["DragonStatue"] = (199.99, "Limited edition crystal dragon")

# Combine catalogs using __add__
mega_catalog = kids_toys + collector_editions

# Access items with __getitem__
print(mega_catalog["RoboDog"])  # (49.99, 'Self-charging robot dog')

# Check existence with __contains__
print("DragonStatue" in mega_catalog)  # True

# Get count with __len__
print(f"Total toys: {len(mega_catalog)}")  # Total toys: 3

# Iterate with __iter__
for name, details in mega_catalog:
    print(f"{name}: {details[1]}")

# String representation with __str__
print(mega_catalog)

# Callable discount with __call__
print("\n🔥 FLASH SALE 🔥")
print(mega_catalog(20))  # 20% off prices

# Remove item with __delitem__
del mega_catalog["MagicKit"]