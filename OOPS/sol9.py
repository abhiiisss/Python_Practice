# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


class Car:

    total_Car = 0


    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_Car += 1

    def fullname(self):
        return f"{self.brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @property
    def model(self):
        return self.__model


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

print(isinstance(tesla, Car))
print(isinstance(tesla, ElectricCar))


Jaguar = Expensive_Car("Jaguar", "MOdel Z", "32,000,000")


# print(my_car.model)

 

