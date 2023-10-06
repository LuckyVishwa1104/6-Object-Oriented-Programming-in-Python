# instance method example 2-

# an employee class having details of employee
class Employee:

    # this is a class variable shared by all objects
    department = "Marketing"

    # parameterzed constructor
    def __init__(self,a,b):
        self.id=a
        self.salary=b

    # method to display the instance variable of respective method
    def show(self):
        print('Employee ID is',self.id)
        print('Employee slaary is',self.salary)
    
    # getter of Emplotyee id
    def get_id(self):
        return self.id
    
    #setter for employee id
    def set_id(self,i):
        self.id=i

    # getter for salary of employee
    def get_salary(self):
        return self.salary

    # setter for employee salary
    def set_salary(self,s):
        self.salary=s

# creating objects fro above calss
obj1=Employee(101,38000)
obj2=Employee(204,42000)

obj1.show()
obj2.show()

# accesing the employee id using getter instance method
print(obj1.get_id())
print(obj1.get_salary())

print(obj2.get_id())
print(obj2.get_salary())

print(obj1.__dict__)
print(obj2.__dict__)

# updating the employee salary using setter instance method
obj1.set_id(1001)
print(obj1.get_id())

obj1.set_salary(53500)
print(obj1.get_salary())

obj2.set_id(2002)
print(obj2.get_id())

obj2.set_salary(63700)
print(obj2.get_salary())

print(obj1.__dict__)
print(obj2.__dict__)