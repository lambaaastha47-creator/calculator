
print("simple calculator")
num1 = float(input("Enter first number: "))
opr = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
if opr == "+":
    print("Result: ", num1 + num2)
elif opr == "-":
    print("Result: ", num1 - num2)
elif opr == "*":
    print("Result: ", num1 * num2)
elif opr == "/":
    if num2 != 0:
        print("Result: ", num1 / num2)
    else:
        print("cannot divide by zero!")
else:
    print("Invalid operator!")