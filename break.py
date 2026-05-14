#take input from user

a = input("Enter a word: ")

#program to check break keyword

for i in a: #iterate for loop
    if (i == "a"): #check if the letter is A
        #display message
        print("A is found in the word")
        break #if it is A then break the loop
    else:
        print("A not found")

    
