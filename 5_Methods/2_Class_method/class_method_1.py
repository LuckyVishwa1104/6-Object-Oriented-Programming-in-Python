"""Class Method - class method are used to manipulate class variables i.e. to access or update class variable.
A class method can be called by both object ae well class, there is no complusion to create a object for execution of class method.
Class methods are created by using special decorator(@classmethod) and instead of self parameter they have cls parameter as reference 
of current entity."""
# we can't access instance variable using class method

# Syntax
'''
calss Class_Name:
    class_variable=XYZ
    
    @classmethod
    def class_method_name(cls,---):
        instance_variables=XYZ
        ----
# calloing class methods
Class_Name.class_method()'''

# class named as Empoyee id defiend
class Employee:
    Id=2355  # class variable

    # constructor
    def __init__(self,a=1000,b=2000):
        self.aa=a
        self.bb=b

    # general or instance method
    def gen_mtd(self):
        self.book="Death of a Salesman"

    # defining a class method
    @classmethod
    def cls_mtd1(cls):
        print(200+300)

    # method to display class variable
    @classmethod
    def cls_mtd2(cls):
        return cls.Id

# acessing the methods using class name i.e. without creating a object
Employee.cls_mtd1()  # 500
print(Employee.cls_mtd2()) # 2355

# accesing using object
obj1=Employee()
obj1.cls_mtd1()
print(obj1.cls_mtd2())