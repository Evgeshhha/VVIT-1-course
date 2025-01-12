class Vehicle:
    make = "asd"
    model = "sdfghj"
    def get_info(self):
        return "Марка:" + self.make + "\nМодель:" + self.model 
class Car(Vehicle):
    fuel_type = "wwww"
    def get_info(self):
        return "Марка:" + self.make + "\nМодель:" + self.model + "\nтип топлива: " + self.fuel_type
veh = Vehicle()
car = Car()
print(veh.get_info())
print()
print(car.get_info())