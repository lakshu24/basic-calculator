def calculator():
    print("Basic Calculator")

    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", num1 + num2)

    elif op == '-':
        print("Result:", num1 - num2)

    elif op == '*':
        print("Result:", num1 * num2)

    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)

        else:
            print("Error: Division by zero.")

    else:
        print("Invalid operator")

calculator()
        

    
