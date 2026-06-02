#using a try and except block to catch a value error
try:    
    number = int(input("Please enter a number: "))
    print("You entered:", number)
#using value error
except ValueError as ex:
    print("Exception:", ex)