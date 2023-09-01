# creating a student data type
# template for class called Student
class Student:
    # __inti__  Initialized function
    # Defining what a student is in the (). aka Attributes
    # self is referring to the object
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation



# OBJECT FUNCTION
    # putting a function in side of a class
    def on_honour_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
