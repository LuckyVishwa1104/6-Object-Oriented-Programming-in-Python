# example 4
# creating a class 
class Employee:

    a=45 # class variable
    b=56  # class variable

    # constructor
    def __init__(self,a,b,c):
        self.aa=a 
        self.bb=b  ### instance variable
        self.cc=c

    # method for concatenation
    def concate(self):
        print(self.aa+self.bb+self.cc)

    # method for addition
    def add(self):
        print(str(self.aa)+str(self.bb)+str(self.cc))

    @classmethod
    def display(cls):
        print(cls.a)
        print(cls.b)

# creating objects for above class
obj1=Employee(10,20,30)
obj2=Employee(100,200,300)
print(obj1.__dict__)

# calling the add and concate method
obj1.concate()
obj1.add()
print(obj1.__dict__)

obj2.concate()
obj2.add()
print(obj1.__dict__)

# calling the display method
obj1.display() # we can access the class variable, but for that we need reference of an object
print(obj1.__dict__)

print(obj1.a)
print(obj1.b)
print(obj1.__dict__)