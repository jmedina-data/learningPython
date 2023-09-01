from Student import Student

student1 = Student("Oscar", "Accounting", 4.0, False)
student2 = Student("Angela", "Cats", 3.4, False)

# using the function in the class
# function called on_honour_roll in Class called Student
print(student1.on_honour_roll())
print(student2.on_honour_roll())