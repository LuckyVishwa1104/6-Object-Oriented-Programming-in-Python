# example 3
# a class can also have data-members as functions/methods

# a class with name as ticket-booking
class Ticket_Booking:
    name="Lucky Vishwakarma"
    age=32    # - - - data-members
    cantact=9876543210

    # a definition with certain variables
    def Flight_Details(self):
        self.fli_name="Air India"
        self.fli_class="Business class"
        self.amount=254000                #- - - method members
        self.source="Mumbai"
        self.destination="New York"

    # data-members
    status="Confirm"
    print("Happy Journey")
    