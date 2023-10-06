# class method example 2
# a class named as vehicle
class Vehicle:
    wheel=4  # class variable

    # default constructor
    def __init__(self):
        self.model="XYZ"
        self.num="ABCD"

    # method to display the values
    def display(self):
        print(self.modle)
        print(self.number)
    
    # a class method. this method will create a class variable
    # a class method only creates a class variable but it can be accessed  by object, but instance variable can't be accessed by class
    @classmethod
    def cls_mtd1(cls):
        cls.avg=9999
        print(cls.avg)  # 'we can create class variable using class method'

# accessing the class method with class name
print(Vehicle.wheel)
Vehicle.cls_mtd1()
print(Vehicle.__dict__)

# creating object for above class
obj1 = Vehicle()
obj2 = Vehicle()
print(obj1.__dict__)
print(obj2.__dict__)

# accesing the class varible and class method using object
print(obj1.wheel)
print(obj1.__dict__)
obj1.cls_mtd1()
print(obj1.__dict__)

# chaging the class variable
print(obj1.avg)
print(obj2.avg)
obj1.avg=9000
print(obj1.avg)
print(obj1.__dict__)
print(obj2.avg)
print(obj2.__dict__)
Vehicle.avg=90
print(Vehicle.avg)
print(obj1.avg)
print(obj2.avg)
print(Vehicle.__dict__)

