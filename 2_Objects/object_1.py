#2) Objects - object are instance of classes, objects are used to intialize the classes.
# objects are the basic entity of OOP, objects are composed of state(all attributes) and behaviours(methods).
# using object we can access the data-members, method members, methods, other classes of a class

#Syntax:    object_name = class_name()

# example 1
# creating a class car with certain parameters
class Car:
    company="FERRARI"
    model="F8 spider"
    price=89500000
    color="Yellow"

# creating the object of class Car with name car_0bj
# object name should be a valid variable
car_obj=Car()
print(car_obj.__dict__)

# using car object we can access data-members
print(car_obj.company)
print(car_obj.model)
a=car_obj.price
print(a)
b=car_obj.color
print(b)
print(car_obj.__dict__)
