#import necessary libraries
from tkinter import *
from datetime import date

#create window
window = Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

#add widgets
#add labels

lbl = Label(text = "Hello there", fg = "white", bg = "#072f5f", height = 1, width = 300)

#add label for getting name as input from user
#use entry widget to create a text box for user to enter details

name_lbl = Label(text = "Full name", bg = "#3895D3")
name_entry = Entry()

#function to display a message
def display ():
    #read input given b user
    name = name_entry.get()
    #declaring a globle variable
    #to make it accessible anywhere in the program
    global message
    message = "Welcome to the Application! \nTodays date is:"

    greet = "hello "+name+"\n"
    #display details in a text box
    #specify where to add details in text box
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

#add a text box widget to display the message
text_box = Text(height = 3)

#add button and give value of command as name of the function
#press button display function will be called automatically
btn  = Button(text = "begin", command = display, height = 1, bg = "#1261A0", fg = "white")

#organize widgets in the window using pack method
lbl.pack()
name_lbl.pack()
name_entry.pack()
text_box.pack()
btn.pack()

window.mainloop()

        
        

