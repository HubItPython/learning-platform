# class ParentClass:
#     # Parent class attributes and methods

# class ChildClass(ParentClass):
#     # Child class inherits from ParentClass
#     # Additional attributes and methods specific to ChildClass

# # Parent class (Superclass)
# class Animal:
#     def __init__(self, species):
#         self.species = species
    


# class parent():
#     def __init__(self,caste,name):
#         self.caste=caste
#         self.name=name

# class child(parent):
#     def __init__(self,name,caste,child_name):
#         super().__init__(caste, name)  # Call base class initializer
#         self.child_name=child_name
#     def child_detail(self):
#         print(f"{self.child_name} {self.caste}")
# father=parent(name="mohit",caste="khanal")
# child=child(child_name="sohit",name="mohit",caste="khanal")
# print(father.name)
# print(father.caste)
# child.child_detail()


# # Child class (Subclass) inheriting from Animal
# class Dog(Animal):
#     def __init__(self, name):
#         # Initializing attributes of the parent class
#         super().__init__('Dog')
#         self.name = name
    
#     def make_sound(self):
#         return "Woof!"

# # Creating an instance of the Dog class
# my_dog = Dog("Buddy")

# # Accessing attributes and methods
# print(f"My dog's name is {my_dog.name}")
# print(f"It is a {my_dog.species}")
# print(f"And it says, '{my_dog.make_sound()}'")





# class A():
#     def h(self):
#         self.x = 10
#         self.y = 20
#         print("x in A:", self.x)  
#         print("y in A:", self.y)  

# class B(A):
#     def j(self):
#         super().h()  
#         print("x in B:", self.x)  
#         print("y in B:", self.y)  

# ob = B()
# ob.j()

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#   x.move()

from abc import ABC,abstractclassmethod
class car(ABC):
    def wheel(self):
        print("4 wheel")
    @abstractclassmethod
    def speed(self):
        pass
class maruti(car):
    def speed(self):
        print("200KM/hr")
o=maruti()
o.wheel()
o.speed()