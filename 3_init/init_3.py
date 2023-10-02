# example 3
# There are three types of init declaration based on arguments passed
class bike:

    # default init constructor - it does not takes any arguoment accept self
    # wherer self refer to thr current object
    def __init__(self):
        self.name="Harley Devison"
        self.gear=7

    # display method to display the data attributes
    def display(self):
        print(self.name)
        print(self.gear)
    
# object creation at this moment init will bw automatically invoked
bike1=bike()
print(bike1.__dict__)
# calling th e display method usong object name
bike1.display()
print(bike1.__dict__)
# the values for the attributes remains same for any object
bike2=bike()
bike2.display()