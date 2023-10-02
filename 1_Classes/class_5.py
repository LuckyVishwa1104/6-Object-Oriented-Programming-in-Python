# example 5
# example to demonstrate complex class generation

# main class with University name 
class University:
    name="Madras University"
    est_code=43533
    state="Chennai"
    contact=9876543210

    # sub-class with deparment name
    class Deparment:
        d1="Mechanical"
        d2="Electrical"
        d3="Computer"
        d4="Civil"

    # sub-class with Faculty anem
    class Faculty:
        name="WERD DO OPMM"
        exp=23
        class Subject:
            sub_name="Physics"
            sub_code=2342
            sub_fees=90000
    
    # sub-class with Student name
    class Student:
        name="omo sml LKSd"
        age=21
        contact=8745963210
        def Address(self):
            self.add_state="Chennai"
            self.add_pincode=913224
            self.add_land_mark="Lighten Bridgh"
            