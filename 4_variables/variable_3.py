# example 3
# creating a class anmed as Car
class Car:

    wheel=4   # this is a class variable

    # constructor -
    def __init__(self,brand="XYZ",modle="M1"):
        self.brand=brand
        self.modle=modle

    # method to display the variables
    def method(self):
        print("Brand is:",self.brand)
        print("Modle is:",self.modle)

# creating the object of class Car
obj1=Car()
obj2=Car()

# while creating object the init method will get called automatically and the respective instance avriable will be added in its namespace
print(obj1.__dict__)
print(obj2.__dict__)

# upDATING THE VALUE OF INSTANCE VARIABLE FOR RESPECTIVE object, from herre onwards the updated value will be considered
obj1=Car("Ferrari","F8 spider") # if we create a new object with same name, previous one will be discarded and the new one will be considered

# changing the instance variable of obj2
obj2.brand="Ford"
obj2.modle="Mustang"

print(Car.__dict__)
print(obj1.__dict__)
print(obj2.__dict__)

# accessing the class variable using object and class
print(Car.wheel)
print(obj1.wheel)
print(obj2.wheel)

# we cant change the class variable using object
obj1.wheel=5
print(obj1.wheel) # at this moment it will create new instance variable for obj1 and add it in its namespace
print(obj1.__dict__)
print(obj2.wheel) 

# we can changge or update the class variable using class only
Car.wheel=6
print(Car.wheel)
print(Car.__dict__)
print(obj1.wheel)
print(obj2.wheel)  # first preference will be given to local namespace, it any variable is present in local namespace it get printed, it not then it will search in global or class namespce
# that why here 6 is displayed as it is present in, local namespace.