# example 5
# creating a class named Car 
class Car:

    wheel=4 # this is a class variable, it is shared by all objects of this class

    # default constructor
    def __init__(self):
        self.company="Ferrari"  # this is a instance variable
        self.modle="F8 spider"  # this is a instance variable
    
    # a method to display the variable
    def display(self):
        print(self.company)
        print(self.modle)

# creating object for above class
o1=Car()
print(o1.__dict__)
# creating second object for above class
o2=Car()
print(o1.__dict__)

# displaying the instance variable
print(o1.company,o1.modle)
print(o2.company,o2.modle)
print(o1.__dict__)
print(o2.__dict__)

# updating the  variables of the objects
o2.company="Mahindra"
o2.modle="Thar"
print(o2.company,o2.modle)
print(o2.__dict__)

# updating the variables of second object
o1.company="Ford"
o1.modle="Mustang"
print(o1.company,o1.modle)
print(o1.__dict__)

# accessing the class variable
print(o1.wheel)
print(o2.wheel)

print(o1.__dict__)
print(o2.__dict__)
print(Car.__dict__)

# displaying the value of class variable 
print(Car.wheel)
Car.wheel=5 # changing the value of class variable. from here onwards the value of class variable will be 5 as it is being changed
print(Car.wheel)
print(o1.wheel)
print(o1.__dict__)

o1.wheel=6 # this create an instance variable for o1 object and not change the value of class variable as it can't be changed by object
print(o1.wheel)
print(o1.__dict__)
print(o2.wheel)
print(o2.__dict__)
print(Car.wheel)
print(o1.wheel)
# __dict__ - it return the dictioinary of variables and their values associated with respective entity
