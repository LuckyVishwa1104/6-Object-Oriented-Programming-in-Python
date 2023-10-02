# example 5
# defautlt parameter constructor - we can also pass the default parameters to the constructor, if no value is passed in object then default value will bw considered

class Drawing:

    # default parameter constructor
    def __init__(self,name="lUCLKY",age=21):
        self.name=name
        self.age=age

    # displaying method
    def display(self):
        print("My name is ",self.name)
        print("Age is",self.age)

# object without any parameter
obj1=Drawing()
obj1.display()

# object eith parameter
obj2=Drawing("niKHil",22)
obj2.display()
