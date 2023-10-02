# Instance method - it work with object, these types of method are used to manipulate data with reference to object.
# for instance methods we generally pass self as a parameter, which indicate that this method belongd to some object
# there are two types of instance methods Accessor(getter) and Mutator(setter)
#1) accessor(getter) - it is used to fetch the value i.e. to get the value of instance variables
#2) mutators(setter) - it is used to update or modify the value i.e. to set or changet the value of instance variables

class Student:

    school="LITAM"

    # a constructor 
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    # method to display the average 
    def avg(self):
        return ((self.m1+self.m2+self.m3)/3)
    
    # accessor/gettor for variable m1
    def get_m1(self):
        return self.m1
    
    # mutator for variable m1
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
   
# creating object for above class
obj1=Student(20,40,70)
obj2=Student(4,7,9)

print(obj1.avg())  # avg is a instance method as it requires object for its execution
print(obj2.avg())

# accesing the value from the get method
print(obj1.get_m3())

# changing the value of variable 
print(obj1.m1)
obj1.set_m1(200)
print(obj1.m1)

# instance emthods can be accessed by objects only and not the class
# print(Student.avg()) -> this will provide an error
