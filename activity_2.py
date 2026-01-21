#Assigning Different Variables
name = 'penguins'
age = 15
is_student = True
weight = 38.5

#Printing different variables and their data types
print("Name: " , name)
print("Data type of name is: " , type(name))

print("Age: " , age)
print("Data type of age is: " , type(age))

print("is_student: " , is_student)
print("Data type of is_student: " , type(is_student))

print("Weight: " , weight)
print("Data type of weight:" , type(weight))  

#Type casting to convert the datatypes of variables
print("\n After type casting...")
age = str(age)
print(age)
print("Data type of age is: " , type(age))

weight = int(weight)
print(weight)
print("Data type of weight is: " , type(weight))