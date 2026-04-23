#correct code

r = int(input("please enter total number of rows: "))

print("Mirror star triangle")

for i in range(1, r + 1):
    for j in range(1, r + 1):
        if(j <= r - i):
            print(' ', end= ' ')
        else:
            print('*', end= ' ')
    print()