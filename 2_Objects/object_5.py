# example 5
# a class of calculator containg different data-members and methods
class Calculator:
    print("Basic Calculator")
    # addition operation
    def add(self,a,b):
        return a+b
    # subtraction operation
    def sub(self,a,b):
        return a-b
    # multiplication operation
    def mul(self,a,b):
        return a*b
    # division operation 
    def div(self,a,b):
        return a/b
    
# creating object of above class
calc=Calculator()
print(calc.add(10,5))
print(calc.sub(50,88))
print(calc.mul(4,8))
print(calc.div(40,8))

# we can create multiple objects for same class
calc2=Calculator() # here calc2 is another object of same class
print(calc.add(40,80))
print(calc2.mul(8,9))

# one more object of same class
calc3=Calculator()  # calc3 is the third object
print(calc3.div(443,0.994))
