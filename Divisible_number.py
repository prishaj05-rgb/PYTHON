numn = int(input("Enter a number (numerator): "))
numd = int(input("Enter a number (denoinator): "))

if numn%numd==0:
    print("\n" +str(numn)+ " is divisible by " +str(numd))
else:
     print("\n" +str(numn)+ " is not divisible by " +str(numd))