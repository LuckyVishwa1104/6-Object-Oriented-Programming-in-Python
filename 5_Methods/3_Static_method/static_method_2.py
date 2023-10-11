# static method example 2
class Employee:
    department='Human Resource'  # class variable

    # default parameterized constructor
    def __init__(self,Eid=None,ename='Someone'):
        self.EId=Eid
        self.Ename=ename

    # an static method to display the salary pf employee
    @staticmethod
    def static_method(sla):
        return f'Emplyee salary is {sla}'
    
    # an static method which displays the class variable
    @staticmethod
    def static_method1():
        print(Employee.department)

# static method can't access the class or instance varaible, hence it cant modify state of object or class
    # static methos for dispalying instance variables
    @ staticmethod
    def static_method2():
        print(obj1.EId)

    # static method for updating instance variable
    @staticmethod
    def static_method3(para):
        obj1.Ename=para
        print(obj1.Ename)

    # static method for changing class variable
    @staticmethod
    def static_method4(para2):
        Employee.department=para2

# calling the static method
print(Employee.__dict__)
print(Employee.static_method(50000))
Employee.static_method1()
obj1 = Employee(3229,'Harry Poter')
print(obj1.__dict__)
Employee.static_method2()
print(obj1.Ename)
Employee.static_method3("Peter Parker")
print(obj1.Ename)
print(obj1.__dict__)
Employee.static_method4('Psychology')
