"""Instance method - these are the methods that work with object that is they are used to manipulate data associated with objects 
Instance method are initiated with object i.e. they require object for execution.
It requires a self argument which is the reference for the current object.
There are two types of instance methods - Accessor(getter) and Mutator(setter)"""

# Accessor(getter) - to access the instance variables
# Mutator(setter) - to set or update the value of instance variable

# a class named as Student with some variables and methods
class Student:
    name='Haward Bussiness School'

    # constructor method - creates three variab;e fpr every object of this class
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    # mehtod to calculate the average of three variable
    def average(self):
        return ((self.m1+self.m2+self.m3)/3)
    
    # getter for m1
    def get_m1(self):
        return self.m1
    
    # setter for m1
    def set_m1(self,a):
        self.m1=a

    # getter for m2
    def get_m2(self):
        return self.m2
    
    # setter for m2
    def set_m2(self,b):
        self.m2=b

    # getter for m3
    def get_m3(self):
        return self.m3
    
    # setter for m3
    def set_m3(self,c):
        self.m3=c

# creating object of above class
obj1 = Student(20,30,40)
obj2 = Student(200,300,400)

# calling the average method 
print(obj1.average())
print(obj2.average())

# accessing the values of instance variables using instance methods(getters)
print(obj1.get_m1())
print(obj1.get_m2())
print(obj1.get_m3())

print(obj2.get_m1())
print(obj2.get_m2())
print(obj2.get_m3())

# updating the values of instance variables
obj1.set_m1(2.2)
print(obj1.get_m1())
obj1.set_m2(3.3)
print(obj1.get_m2())
obj1.set_m3(4.4)
print(obj1.get_m3())

obj2.set_m1(200.2)
print(obj2.get_m1())
obj2.set_m2(300.3)
print(obj2.get_m2())
obj2.set_m3(500.5)
print(obj2.get_m3())
