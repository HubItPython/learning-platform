
# In Python, there are mainly three types of inheritance:

# Single Inheritance: A class inherits from only one base class. For instance:

# class BaseClass:
#     # Base class definition

# class DerivedClass(BaseClass):
#     # Derived class inherits from BaseClass
# Multiple Inheritance: A class can inherit from multiple base classes. For instance:

# class BaseClass1:
#     # Base class 1 definition

# class BaseClass2:
#     # Base class 2 definition

# class DerivedClass(BaseClass1, BaseClass2):
#     # Derived class inherits from both BaseClass1 and BaseClass2
# Multilevel Inheritance: This occurs when a derived class is created from another derived class. For instance:

# class BaseClass:
#     # Base class definition

# class DerivedClass(BaseClass):
#     # Derived class inherits from BaseClass

# class FurtherDerivedClass(DerivedClass):
#     # FurtherDerivedClass inherits from DerivedClass, which already inherits from BaseClass

# Single Inheritance
class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):  # Dog inherits from Animal
    def make_sound(self):
        print("Bark!")

dog = Dog()
dog.make_sound()  # Outputs: Bark!

# Multiple Inheritance
class Fly:
    def fly(self):
        print("I can fly!")

class Swim:
    def swim(self):
        print("I can swim!")

class Duck(Fly, Swim):  # Duck inherits from both Fly and Swim
    pass

duck = Duck()
duck.fly()  # Outputs: I can fly!
duck.swim()  # Outputs: I can swim!

# Multilevel Inheritance
class Vehicle:
    def vehicle_info(self):
        print("This is a vehicle")

class Car(Vehicle):  # Car inherits from Vehicle
    def car_info(self):
        print("This is a car")

class ElectricCar(Car):  # ElectricCar inherits from Car, which already inherits from Vehicle
    def electric_info(self):
        print("This is an electric car")

electric_car = ElectricCar()
electric_car.vehicle_info()  # Outputs: This is a vehicle
electric_car.car_info()  # Outputs: This is a car
electric_car.electric_info()  # Outputs: This is an electric car
