# static method - these are the method that have no effect on instance and class variable, it is used to perform external application
# it is like simple function and doesn't require ant reference(self, cls) for execution

#syntax
'''class class_name:
        class_var=xyz

        def __init__(self):
            pass
            
        @ staticmethod
        def static_method():
            pass
            
    obj1.static_methos1()
'''
# class na,ed as student
class Student:
    name="University of Dallas" # class variable

    # static method to display the details of School
    @staticmethod
    def staic_method1():
        print(Student.name)
        print('Id is',33049)
        print("Admotted to Economics Studies")

# static method can be accessed by class as well as object 
# accessing using class
Student.staic_method1()

# accessing using object
obj1 = Student()
obj1.staic_method1()
