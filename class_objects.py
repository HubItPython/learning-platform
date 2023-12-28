# class ClassName:
#     # Class variables
#     variable = 'value'
    
#     # Constructor method
#     def __init__(self, parameters):
#         self.attribute = parameters  # Initializing instance attributes
        
#     # Other methods
#     def method_name(self, other_parameters):
#         # Method body
# # Creating an object of class ClassName
# obj = ClassName(parameters)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)

# del p1.age

# class Person:
#     # Class variable
#     species = "Human"

#     # Constructor method
#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age    # Instance attribute

#     # Method to greet
#     def greet(self):
#         return f"Hello, my name is {self.name} and I'm {self.age} years old."

# # Creating objects of the Person class
# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)

# # Accessing attributes
# print(person1.name)        # Output: Alice
# print(person2.age)         # Output: 25
# print(person1.species)     # Output: Human

# # Accessing methods
# print(person1.greet())     # Output: Hello, my name is Alice and I'm 30 years old.
# print(person2.greet())     # Output: Hello, my name is Bob and I'm 25 years old.

class A():
    def __init__(self,aname):
        self.name=aname
        print(self.name)
obj=A("mohit")