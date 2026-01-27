#Take marks as input from user
print("Enter marks obtained from 4 subjects: ")
math = int(input("Maths: "))
science = int(input("Science: "))
english = int(input("English: "))
hindi = int(input("Hindi: "))

#Lets calcutae the percentage of marks
sum = math+science+english+hindi
print ("Sum of math,english,hindi, and science")

perc = (sum/400) * 100

print(end= "Percentage Mark = ")
print(perc)