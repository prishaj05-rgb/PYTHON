import random #importing module
playing = True #initialiseing variable
number = str(random.randint(1,9)) #generating random number

print("I will generate a number between 1 and 9. You have to guess it.") #printing message
print("The game ends when you get 1 hero!")


#iterate loop till the condition is true
while playing:
    guess = input("Enter your guess: \n") #taking input from user
    if number == guess:
        print("you win")
        print("The number was: ", number)
        break

    else:
        print("Your answer is wrong. Try again!")