from tkinter import *
from datetime import date

window = Tk()
window.title("Welcome to the Workshop")
window.geometry("400x300")

lbl = Label(text = "Hello and welcome", fg = "white", bg = "#072f5f", height = 1, width = 300)

name_lbl = Label(text = "Please enter your full name", bg = "#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the Workshop! \nToday's date is:"

    greet = "Hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box = Text(height = 3)

btn = Button(text = "Start", command = display, height = 1, bg = "#1261A0", fg = "white")

lbl.pack()
name_lbl.pack() 
name_entry.pack()
text_box.pack()
btn.pack()

window.mainloop()