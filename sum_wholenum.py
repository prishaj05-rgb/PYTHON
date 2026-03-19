#input integer value
n = int(input("Enter the number whose sum you want to find:"))
sum = 0

#iterates for n+1 times: i=1 to n+1

for i in range(1, n):
    sum = sum + 1
    print("\n Sum = ", sum)