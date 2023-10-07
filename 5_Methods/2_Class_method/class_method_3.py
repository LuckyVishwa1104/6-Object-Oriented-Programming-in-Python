# example of class emthod 3
# a class method can be created without decorator
class Student:

    school='Haward Business School'  # class variable

    # parameterized constructor
    def __init__(self,id,s_class):
        self.id=id
        self.s_class=s_class

    # an class method to create a class variable
    def cls_mtd1(cls,loc):
        cls.location=loc

    # a class emthod to display the class variables
    def cls_mtd2(cls):
        print(cls.location)
        print(cls.school)

print(Student.__dict__)
# creating class method using classmethod function
Student.cls_mtd1 = classmethod(Student.cls_mtd1)
Student.cls_mtd2 = classmethod(Student.cls_mtd2)

# calling the class emthod
Student.cls_mtd1("INDIA")
Student.cls_mtd2()

# calling using object name
obj1 = Student(2330,'BE')
obj1.cls_mtd1("Dallas")
obj1.cls_mtd2()

# we can also add an class method defined outside of class to class
def cls_mtd3(cls):
    return cls.location

Student.cls_mtd3 = classmethod(cls_mtd3)
print(Student.cls_mtd3())
print(Student.__dict__)
