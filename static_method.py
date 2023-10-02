# static mehtod - these are the methods which have no effect of instance or class variables, it has nothing to do with class or insstance variable
# it is used for external application, it doesn't require any reference parameter like self or cls for execution
# ti is like simple functions which executes some tasks

# syntax-
'''class class_name:
        def __init__(self):
            pass
        
        @staticmethod
        def method_name():
            pass
    
    class_name.method_name()
'''
class Student:

    school="HBS"

    # canstructor or instance method
    def __init__(self):
        pass

    # a static method displaying class information
    @staticmethod
    def info():
        print("this is a static method")

    # a static method to display the sum of two number
    @staticmethod
    def info1(a,b):
        return a+b

# it doesn't require any refernce argument for execution
Student.info()
print(Student.info1(23,10,20))

# static methods can be accessed by object and class name as well
obj1=Student()
print(obj1.info1(45,100,200))




