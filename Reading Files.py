

# open( "name of file or path to file", "r")

# "r"  "w"  "a"  "r+"
# r read
# w write
# a append
# r+ read and write

#variable_name = open("name of file", "r")
# always close a file after opening it
#variable_name.close()

employee_file = open("employee.txt", "r")
# check to see if the file is readable ie the "r"
print(employee_file.readable())
# reads the whole file
print(employee_file.read())
# reads a specific line in the file
print(employee_file.readline())

employee_file.close()


# puts the lines in an array
employee_file = open("employee.txt", "r")
print(employee_file.readlines())
employee_file.close()