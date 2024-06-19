operator = input("Enter an operator : ")
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))


def calculator(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    else:
        return "Invalid Operator"


print(f"The result of {operator} operation is ",calculator(operator, a, b))

