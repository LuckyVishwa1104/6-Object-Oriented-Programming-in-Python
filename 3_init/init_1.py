# __init__() method - the __inti__ method is a special method, it is the default constructor of the class
# the task of __init__ is to assign the values to the attributes of class when an object is created
# it get called autometically when an object is created

# syntax:
'''class class_name:
    def __init__(self,arguments,..):
        self.arg1=arg1
        self.arg2=arg2
        ----
        self.argn=argn
'''

# example 1
class Person: # Person is a class

    # an init method with self as a parameter where self points to currrent object
    # here self is a parameter which points to the current object
    def __init__(self):
        self.name="Lucky"
    
    # this a method that displays the values
    def display(self):
       print(self.name)

# object obj1 is created
obj1=Person() # at this instance init is called
obj1.display()

# obj2 is also created for the same class
obj2=Person() # here again init will be called
obj2.display()

"""Code explanation: 
a class Person is created, in which init and display methods are declaerd. Two objects of the class Person are created obj1 and obj2.
the two methods are passed with self as a parameter, which points to the current object.
while executing line 18: obj1 is created and init is called automatically i.e. obj1=Person() ~ Person.__init__(obj1) 
so during calling the init methood it will be def __init__(obj1): where obj1 is referenced as self. hence obj1.name="Lucky".
similarly at line 19 display method is called obj2.display() ~ obj2.display(obj2), by default it has a parameter as current object referenced
so at calling part it will be def display(obj1): print(obj1.self)"""
