class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def getinfo(self):
        return self.make,self.model
class Car(Vehicle):
    def __init__(self, fuel_type):
        self.fuel_type=fuel_type
    def getinfo(self):
        return self.fuel_type
s=Vehicle('lada','vesta')
print(Vehicle.getinfo(s))
s=Car('92')
print(Car.getinfo(s))
