# example 5
# here is a class with some attributed(state) and methods(behaviours)
class Vehicle:
    print("This is a Vehicle class")
    def two_wheeler(self,opt1,opt2):
        self.opt1=opt1
        self.opt2=opt2
        print(f"You have to options {self.opt1} and {self.opt2}")
    def four_wheeler(self,opt1,opt2):
        self.opt1=opt1
        self.opt2=opt2
        print(f"You have to options {self.opt1} and {self.opt2}")

# creating object of vehicle class
v1=Vehicle()
v1.two_wheeler("Bullet","sports")
v1.four_wheeler("Ferrari","Porche")

# we can create multiple objeects for same class
v2=Vehicle()
v2.four_wheeler("Thar","RangeRover")
v2.two_wheeler("Pulsor","CD delux")
