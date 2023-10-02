# Class method - these are the method which are used to deal with class variables
# they require decorators for there execution, we can call class method without creating any object
# class mrthod can be accessed by both object and class as well
#syntax
'''class class_name:
        class_varaible=xyz
        @classmethod
        def method_name(cls):
            cls.aa=class_variable
        
    print(class_name.method_name())'''

# class
class Employee:
    # class variable
    univercity="The open Univercity"  # class variable

    # consturctor -
    def __inti__(self,a,b):
        self.aa=a 
        self.bb=b
    
    # method ot display class variable
    @classmethod  # this is a decorator necessory for class method
    def info(cls):
        return cls.univercity
    
    # class method
    @classmethod
    def info2(cls):
        cls.m=89
        cls.n=90
        print(cls.m+cls.n)

    # class method to add three numbers
    @classmethod
    def info3(cls,x,y,z):
        cls.x=x
        cls.y=y
        cls.z=z
        return (x+y+z)

obj1=Employee() 
# while calling the class method we need to use calss name instead of object name
print(Employee.info())
Employee.info2()
print(Employee.info3(10,20,30))

# using objects we can access the class methods and variable declare in that mehtod
print(obj1.x)
print(obj1.y)
print(obj1.z)

print(obj1.info3(1,2,3))
