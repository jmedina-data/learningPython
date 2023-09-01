
# is statements with comparisons
# can compare numbers or strings or booleans

# >= greater than or equal to - is a comparison operator
# other comparison operators : ==, != not equal, <, >, >=, <=
def max_num(num1, num2, num3):
    # comparing num1 to num2 and num3
    if num1 >= num2 and num1 >= num3:
        return num1
    # comparing num2 to num1 and num3
    elif num2 >= num1 and num2 >= num3:
        return num2
    # num 3 is the biggest
    else:
        return num3


print(max_num(3456, 40, 5))