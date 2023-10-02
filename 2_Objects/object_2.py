# example 2
# creating a class named as laptop
class laptop:
    brand="Dell"
    model="G 15"
    color="Shadow Black"
    price=69000
    def processor(self):
        print("Intel core i5 12 gen")
        print("Intel Iris XE graphics")
        print("Clock speed - 4.7 GHz")
    
# creating object of class
laptop_obj = laptop()
print(laptop_obj.__dict__)

# accessing the data-members and method members of class
print(laptop_obj.brand)
print(laptop_obj.model)
print(laptop_obj.color)
print(laptop_obj.price)
# accessing the method members
laptop_obj.processor()
