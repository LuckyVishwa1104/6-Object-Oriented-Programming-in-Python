# Object Oriented programming - Python supports object oriented programming features. In object oriented programming paradigm everything is moulded in object.
#It has modular programming approach, in which data and function are bounded in single entity are called as class.

#1). Class - class are the blue print for the creating objects. they are collection of data-members and method members
# class defines data-type with variable, properties and methods, a class is declared with class keyword
# class_name is a valid variable and statements can be a data-members and member methods or other class also
'''Syntax:
        class class_name:
            statement 1
            statement 2
            - - - 
            statement n
'''
#example -1.
# a class of car with its properties

# a class with name car is declared, class name should always start with capital letter
class Car:   # declaring a class
    brand="FERRARI"    
    model="F8 Spider"   # data-members
    # variables of a class are knowns as attributes
    color="Yellow"
    price=85900000
# class ended here

# here is another class with some data-members and methods
class Smart_Phone():
    modle="Nothing Phone 1"
    brand="Nothing"
    price=53000
    def specification(self): # specification() is a method member
        self.camera="64 px"
        self.processor="Snapdragon Gen1+"
        self.battery=5000
        self.charger="55W"
