#take 2 inputs from users

lower = int(input("enter a lower range"))
upper = int(input("enter a upper range"))

print("Prime numbers between ", upper, "and" ,lower, "are: ")

#iterate loop from lower limit to upper limit

for num in range (lower, upper + 1): 
    #all prime numbers are greater than 1
    if num > 1: 
