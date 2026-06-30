def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operation = input("Choose which operation to perform (add,subtract,multiply,divide): ")



try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    if operation == "add":
    
        print("The sum of", num1, "and", num2, "is", add(num1, num2))

    elif operation == "subtract":
   
     print("The difference of", num1, "and", num2, "is", subtract(num1, num2))
    elif operation == "multiply":
    
        print("The product of", num1, "and", num2, "is", multiply(num1, num2))
    elif operation == "divide":
        try:
       
            print("The quotient of", num1, "and", num2, "is", divide(num1, num2))
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

except ValueError:
    print("Invalid input. Please enter numeric values.")
else:
    print("Invalid operation selected")

