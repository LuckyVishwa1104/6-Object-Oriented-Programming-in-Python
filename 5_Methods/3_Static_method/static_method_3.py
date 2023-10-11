# static method example 3
# A CUSTOMER NAMED CLASAS with member method and data member
class Customer:
    region = 'Brazil'

    # a constructor 
    def __init__(self):
        self.cid=101
        self.cname="Jhon Cena"

    # a static method to display message
    @staticmethod
    def sta_met1():
        print("This is a Static method!")
        
    @staticmethod
    # another static method
    def sta_met2():
        name="Lucky"
        return name
    
    @staticmethod
    # static method using data from another static method
    def sta_met3(aa):
        print("Hello",aa,"How are you")

# creating object for above class
obj1 = Customer()

# acessing static method by object name
obj1.sta_met1()
obj1.sta_met3(obj1.sta_met2())

