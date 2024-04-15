# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

#(to private any thing in oops u have to just use double underscore)
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self): #getter to get the call the private value
        return "Your Car brand is " + self.__brand

    def fullname(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size



tesla = ElectricCar("Tesla", "Model S", "85kWH")
print(tesla.model)

print(tesla.fullname())

print(tesla.get_brand())
     
