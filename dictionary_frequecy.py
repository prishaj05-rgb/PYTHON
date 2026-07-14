test_dict = {'Codingal' : 2, 'is' : 3, 'best' : 2, 'for' : 2, 'learning' : 3, 'coding' : 1}

print("Original Dictionary : " + str(test_dict))

K = int(input("Enter the value to find frequency : "))

res = 0

for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("frequency of K is : " + str(res))
