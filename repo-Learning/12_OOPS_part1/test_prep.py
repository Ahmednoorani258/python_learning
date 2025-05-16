class Car:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def start(self):
        print(f"{self.brand} {self.model} has started.")
        
    def stop(self):
        print(f"{self.brand} {self.model} has stopped.")
        
    def __del__(self):
        print(f"{self.brand} {self.model} has been destroyed.")
        
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.start()
car2.start()

car1.stop()
car2.stop()

del car1
del car2
        
        
