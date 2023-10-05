# A class have variables defined in it, there are two types of variables in a class.
''' 1) Class variable: 
these variable are the variable defined in the body of class, these variables are shared by all the object of the class.
it can be changed by only the class, each object can access these variables. '''
'''2) Instance variable:
these are the variable defined in particular methods, they belong to that method only, no object can access the instance variables of other object'''

# example 1
# class named as exapmle
class Example:

    species="Human"  # class variable
    planet="earth"   # class variable

    # init methid constructor
    def __init__(self,name,age):
        self.name=name # instance varible
        self.age=age  # instance variable

    # method to display
    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
    
# creaating objects for above class
obj1=Example("Lucky",21)
obj2=Example("Nikhil",22)

# while object creatoing, init will be called and respective instance variable will be created for these objects
print(obj1.__dict__)
print(obj2.__dict__)
print(Example.__dict__)

# as the class variaable are accessible to all the objects
print(obj1.species)
print(obj1.planet)

print(obj2.species)
print(obj2.planet)

# it will not get added in instance namespace as it is class variable
print(obj1.__dict__)
print(obj2.__dict__)
