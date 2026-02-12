a = 10
b = 12
c = 0

#And means all conditions must be true

if a and b and c:
    print("All numbers have boolean values as true")

else:
    print("At least one number has boolean value as false")


a = 10
b = -10
c = 0

#If even one of the answers is true, the statement is true 
if a > 0 or b > 0:
    print("Either number is greater than 0")

else:
    print("No number is greater than 0")


if b > 0 or c > 0:
    print("Either of the number is greater than 0")

else:
    print("No number is greater than 0")