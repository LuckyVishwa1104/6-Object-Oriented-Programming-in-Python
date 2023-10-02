# example 3
# creating a class named as Ticket_Boooking

class Ticket_Booking:
    name="Lucky Vishwakarma"
    age=32    # - - - data-members
    cantact=9876543210

    # method definition with certain variables
    def Fligh_Details(self):
        fli_name="Air India"
        fli_class="Business class"
        amount=54000                #- - - method members
        source="Mumbai"
        self.destination="New York"
        print(fli_name)
        print(amount)
        print(fli_class)
        print(source)
        #print(destination)

    # data-members
    status="Confirm"
    print("Happy Journey")

# creating object of ticket booking class
ticket = Ticket_Booking()

# accessing the data-members of ticket class
print(ticket.age)
print(ticket.cantact)
print(ticket.name)
print(ticket.status)
