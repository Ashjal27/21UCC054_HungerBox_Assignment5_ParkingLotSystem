class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate

class Bike(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)

class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)

class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)