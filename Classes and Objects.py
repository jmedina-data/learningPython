# USE STUDENT.PY
# class is a data type. you can define it.
# an Object is the actual data type being made
# in this case the Object is the student

#     Student file    Student class    they are just called the same thing
from Student import Student

# Creating Student object
student1 = Student("Jim", "Business", 2.9, True)
student2 = Student("Pam", "Art", 3.0, False)


print(student1.is_on_probation)
print(student1.gpa)