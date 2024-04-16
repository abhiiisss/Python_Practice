# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:

    total_Car = 0


    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_Car += 1

    def fullname(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"



class Expensive_Car(Car):
    def __init__(self, brand, model, Car_budget):
        super().__init__(brand, model)
        self.Car_budget = Car_budget

    def fuel_type(self):
        return"Power Petrol"

    def fullname(self):
        return f"{self.brand} {self.model} {self.Car_budget}"


my_car = Car("Tata", "Nexon")

tesla = ElectricCar("Tesla", "Model S", "85kWH")


Jaguar = Expensive_Car("Jaguar", "MOdel Z", "32,000,000")
# print(tesla.model)

# print(tesla.fullname())



# print(my_car.fuel_type())
# print(tesla.fuel_type())

#print(tesla.total_Car)

print(Jaguar.fullname())

print(Jaguar.Car_budget)

print(Car.total_Car)
     
