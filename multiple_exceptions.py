try:
    num1,num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1/num2
    print ("result is", result)
    #using multiple except block for different type of error

except ZeroDivisionError:
    print("Division by zero is error")

except SyntaxError:
    print("comma is missing enter numbers like this 1,2,3")

except:
    print("wrong input")

else:
    print("no exceptions")

finally: 
    print("This will always print no matter what")
