from tkinter import *
import string
from random import *

smallFont = ["Courier", 14]
avenir = ["Avenir", 14]
bgColor = "#FAF6F6"
textColor = "#000000"


#button function that occurs when button is pressed
def showPassword():
    try:
        length = int(entry.get())
        password = str(length)
        pwBox.configure(text = "Generated password: " + password)
        pwBox.pack()
    except ValueError:
        pwBox.configure(text = "Input has to be a number. Try again")
        pwBox.grid(row = 5)


#Create GUI for a window
window = Tk()
window.geometry("400x400")
window.resizable(0,0)
# window.pack_propagate(0)

window.title("Password generator")
upperCase = IntVar()
upperCaseCheckBox = Checkbutton(window, text = "UpperCase letter", variable = upperCase)

number = IntVar()
numberCheckBox = Checkbutton(window, text = "Number: 1234567890", variable = number)

symbol = IntVar()
symbolCheckBox = Checkbutton(window, text = "Symbol: !@#$%^&*()_-+=", variable = symbol)

label = Label(window, text = "Length of password:")
entry = Entry(window)
btn = Button(window, text ="Generate", command = showPassword)
pwBox = Label(window)


#Configure & format widgets
window.config(bg = bgColor)
label.config(bg = bgColor, fg = textColor, font = avenir)
entry.config(bg = bgColor, font = avenir)
btn.config(bg = bgColor, font = avenir)
pwBox.config(bg = bgColor, font = avenir)
upperCaseCheckBox.config(bg = bgColor, font = avenir)
numberCheckBox.config(bg = bgColor, font = avenir)
symbolCheckBox.config(bg = bgColor, font = avenir)

#Add all to window
upperCaseCheckBox.grid(row = 0, sticky = W)
numberCheckBox.grid(row = 1, sticky = W)
symbolCheckBox.grid(row = 2, sticky = W)
label.grid(row = 3, sticky = W)
entry.grid(row = 3, column = 1)
btn.grid(row = 4, ipady = 5, ipadx = 5, pady = 5)

window.mainloop()
