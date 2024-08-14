def calculator():
    
    num1=int(input("Enter the first number:"))
    operation=input("Enter an operation (+,-,*,/):")
    num2=int(input("Enter the second number:"))

    if operation== '+':
        result = num1 + num2
        print(f"The answer is: {result}")

    elif operation== '-':
        result = num1 - num2
        print(f"The answer is: {result}")

    elif operation== '*':
        result = num1 * num2
        print(f"The answer is: {result}")

    elif operation== '/':
        if num2 !=0:
            result = num1 / num2
            print(f"The answer is: {result}")
        
        else:
            print("Error")

    else:
        print("Invalid operation!")
        
calculator()