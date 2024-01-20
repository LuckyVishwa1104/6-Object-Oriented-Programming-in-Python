# example 2
# an object can change the values of attributes of calss
# an object can have different values for attributes of class and these values are assigned to the attributes through __init__ method

class Student: # a class Student is created 

    # cinstructor function or method
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # another method to display values
    def display(self):
        print("Name =",self.name,"Age =",self.age)

# first object wiht some values
stud1=Student("Lucky",21)
# second object with some other values
stud2=Student("Nikhil",21)

# calling the display method with both the object
stud1.display()
stud2.display()