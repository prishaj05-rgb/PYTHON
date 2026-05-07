def add(P,Q):
    #this function is made to add two numbers
    return P + Q
def subtract(P,Q):
     #this function is made to subtract two numbers
     return P - Q
def multiply(P,Q):
     #this function is made to multiply two numbers
     return P * Q
def divide(P,Q):
     #this function is made to divide two numbers
     return P / Q

#now we will take inputs from the user

print("Please select the operation")
print("a. ADD")
print("b. SUBTRACT")
print("c. MULTIPLY")
print("d. DIVIDE")

choice = input("PLease enter choice (a/b/c/d)")

num1 = int(input("please enter number 1: "))
num2 = int(input("please enter number 2: "))

if choice == 'a':
     print (num1, '+', num2, '=', add(num1, num2)  )

elif choice == 'b':
     print (num1, '-', num2, '=', subtract(num1, num2)  )

elif choice == 'c':
     print (num1, '*', num2, '=', multiply(num1, num2)  )

elif choice == 'd':
     print (num1, '/', num2, '=', divide(num1, num2)  )

else:
     print("your input is invalid")