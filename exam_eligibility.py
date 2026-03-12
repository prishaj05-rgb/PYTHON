#take input for the student that he can attend the exam or not

med_cause = input("Did you have a medical cause (Y/N): ").strip().upper()

#checking the user input and predicting output accordingly

if med_cause == 'Y': #condition 1
    print("You are allowed")
else: 
    #take input of the attendance 
    atten = int(input("Enter the attendance of the school:" ))

    if atten >= 75: #condition 2
        print("Allowed")

    else:
        print ("Not Allowed ")