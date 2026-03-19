#Input a word or a sentence
string = input("Please enter your own string")

string2 = ('')

#loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nthe original string = " ,string)
print("the reverse string" , string2)