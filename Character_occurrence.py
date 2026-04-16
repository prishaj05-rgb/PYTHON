#Take input of word

string = input("Please enter your word: ")

#Take input of character

char = input ("Please enter your own character ")

i = 0
count = 0

#loop will find the occurrence of character

while (i < len(string)): #string operation

    if(string[i] == char): #condition 1
        count = count + 1
    i = i + 1

#Display results

print("The total number of times ",char, "Has occurred =", count)