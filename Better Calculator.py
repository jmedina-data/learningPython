
# float immediately turns it into a number
num1 = float(input("Enter first number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter second number: "))

# first figure out what the op (operator) is
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")