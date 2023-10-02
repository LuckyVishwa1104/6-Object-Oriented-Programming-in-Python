# example 4
# parameterised init constructor - it accepts several parameters, for each parameter we need to declare data-members in init method

class efault:

    # parameterised init connstructor
    def __init__(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3

    # sumation method
    def add(self):
        print(self.a1+self.a2+self.a3)
        #return self.a1+self.a2+self.a3
    
# object with parameters
obj=efault(34,56,77)
obj.add()

# object of same class with some other parameters
obj2=efault(99,59,39)
obj2.add()
