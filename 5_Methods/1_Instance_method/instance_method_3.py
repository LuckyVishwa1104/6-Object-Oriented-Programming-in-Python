# instance method example 3
# creating instance variable using instance method other than constructor

# a class named as student
class Student:

    uni='Uni of Dallas'  # class variable

    # default parameterized constructor
    # this method will create instance variables
    def __init__(self,roll=2302,age=20):
        self.roll=roll
        self.age=age

    # an additional method to create instance variable
    def create(self,mark):
        self.mark=mark

    # an instance method to display inastance variables
    def dis(self):
        print('Roll number is',self.roll)
        print('Age is',self.age)
        print('Grade is',self.mark)

# creating object for above class
obj1 = Student()
obj2 = Student(2303,21)
print(obj1.__dict__)
print(obj2.__dict__)

# calling the instance method
obj1.create(94)
obj2.create(92)
print(obj1.__dict__)
print(obj2.__dict__)

# displaying the values ofinstance variables
obj1.dis()
obj2.dis() 
