# example 2
# creating a class named as Sample
class Sample:

    number=23  # class variable
    
    def __init__(self,num1,num2):
        self.num1=num1  # instance variable
        self.num2=num2  # instance variable
    
    # method to add the numbers
    def add(self):
        print(f'{self.num1} + {self.num2} = {self.num1+self.num2}')

# creating the objects of the class
obj1=Sample(10,20)
obj2=Sample(100,200)

# displaying the content of namespaces
print(Sample.__dict__)
print(obj1.__dict__)
print(obj2.__dict__)

# callkng the add method of the Sample class
obj1.add()
obj2.add()

# accessing the class variable
print(Sample.number)
# as it is a class variable it will not get added in the instance namespace of the objects
print(obj1.number)
print(obj2.number)

# instance variable get updated for respective oibject, from here onwards the value will be this only i.e. the updated one
obj1.num2=40
print(obj1.__dict__)
obj1.add()

obj2.num1=1000
obj2.num2=2000
print(obj2.__dict__)
obj2.add()

# here a new instance variable is created for obj1 object of Sample class and it will get added in its namespace
obj1.num3=80
print(obj1.__dict__)
# similarly for object obj2
obj2.num3=4000
print(obj2.__dict__)
