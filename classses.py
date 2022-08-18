"""
write classes that represent real-world things and situations
then, create objects based on these classes

classes, define the general behavior that a whole category of objects can have.
when you create individual objects from the classes, each objects is automatically equipped with the general behavior

making an object from a class is called instantiation , you work with instance of a class
you will specify the kind of information that can be stored in instance
you will define actions that can be taken with these instances
you will write classes that extend the functionality of existing classes
you will store your classes in modules and import classes written by other programmers
"""

'''
__init__() => a special method that python runs automatically whenever we create a new instance based on dog class
self parameter is required in the method definition, and it must come first before the other parameters. because
    it is a reference to the instance itself. it gives the individual instance access to the instance of class 
self.name = name takes the value associated with the parameter name and assign it to the variaable naame 
'''


# creating a class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} sit")

    def roll_over(self):
        print(f"{self.name} roll-over")


# making an instance


my_dog = Dog("Willie", 6)
print(f"my dog name is {my_dog.name}")
print(f"he is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

""" when an instance is created , attributes can be defined without being passed in as parameters"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.gas_size = 12

    def read_odometer(self):
        print(f"this car has {self.odometer} miles on it")

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        self.odometer = mileage

    def fill_gas_tank(self):
        print(f"this car has {self.gas_size} gallon")


# changing the attributes
my_new_car = Car('audi', 'a4', 2022)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer = 23
my_new_car.read_odometer()

my_new_car.update_odometer(88)
my_new_car.read_odometer()

my_new_car.fill_gas_tank()

"""
inheritance
when one class inherits from another , it takes on the tributes and methods of the firsst class
the original class is called parent class, and the new class is the child class

you can add any new attributes and methods necessary to differentiate the child class from the parent 

you can override any method from the parent class
    you define a method in the child class with the same name aas the method you want to override in the parent class
    python will disregard the parent class method and only display the message that you define in the child classs

"""


class ElectricCar(Car):  # place the parent class inside parenthesis
    def __init__(self, make, model, year):  # takes in the information required to make a car instance
        super().__init__(make, model, year)  # use super() to inherit any or all of the attributes and methods of its parent class
        # self.battery_size = 77  you can add any new attributes and methods necessary to differentiate the child class from the parent
        self.battery = Battery()  # this line tells python to create aa new instance of Battery


    def describe_battery(self):
        print(f"the battery is {self.battery_size} kWh")

    def fill_gas_tank(self):
        print("this car doesn't need a gas tank")


# you can break your class into smaller classes

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"the battery is {self.battery_size} kWh")


my_tesla = ElectricCar('tesla', 'model s', 2021)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()  #
my_tesla.fill_gas_tank()



'''
you can store classes in modules and then import the classes you need into your main program


ex: 
car.py
    class Car
    class Battery
    class ElectricCar(Car)
    

my_car.py
    from car import Car  => open the car module and import car class
    
my_electric_car.py
    from car import ElectricCar
    
    
or 
 from car import Car, ElectricCar
 
 or 
 import car =>import entire car module
 
or 
from car import * --> import all classes from a module


 
 


'''