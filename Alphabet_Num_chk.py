c = (input("Enter a Character: "))

if c>= '0' and c<= '9':
    print("\nThis is a number")
elif c>= 'a' and c<= 'z':
    print("\nThis is an alphabet")
elif c>= 'A' and c<= 'Z':
    print("\nThis is an alphabet")
else:
    print("\nThis is not an Alphabet nor a Number")