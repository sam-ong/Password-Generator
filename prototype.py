from tkinter import *
import string
from random import *

smallFont = ["Courier", 14]
avenir = ["Avenir", 14]
bgColor = "#F9EEF5"
textColor = "#000000"


#button function that occurs when button is pressed
def showPassword():
    try:
        length = int(entry.get())
        if length < 6:
            pwBox.configure(text = "Length too short!")
            pwBox.grid(row = 5, columnspan = 2, ipady = 10)
            entry.delete(0,END)
            return
        elif length >14:
            pwBox.configure(text = "Length too long!")
            pwBox.grid(row = 5, columnspan = 2, ipady = 10)
            entry.delete(0,END)
            return
        password = generatePassword(length)
        pwBox.configure(text = "Generated password: " + password)
    except ValueError:
        pwBox.configure(text = "Input has to be a number")
        entry.delete(0,END)
    pwBox.grid(row = 5, columnspan = 2, ipady = 10)

def generatePassword(length):
    wordLength = length-2
    if number.get() == 0: wordLength += 1
    if symbol.get() == 0: wordLength += 1

    try:
        with open ("words.txt", "r") as file:
            words = set(file.read().split())
            words1 = []
            for word in words:
                if len(word) == wordLength:
                    words1.append(word)
            password = choice(words1)
            if number.get() == 1:
                password += str(choice([0,1,2,3,4,5,6,7,8,9]))
            if upperCase.get() == 1:
                password = password.title()
            if symbol.get() == 1:
                password += str(choice(string.punctuation))
            return password
    except IOError:
        return "FILE LOAD ERROR"

#Create GUI for a window
window = Tk()
window.geometry("400x300")
window.resizable(0,0)
window.grid_propagate(0)

window.title("Password generator")
upperCase = IntVar()
upperCaseCheckBox = Checkbutton(window, text = "UpperCase letter", variable = upperCase)

number = IntVar()
numberCheckBox = Checkbutton(window, text = "Number: 1234567890", variable = number)

symbol = IntVar()
symbolCheckBox = Checkbutton(window, text = "Symbol: !@#$%^&*()", variable = symbol)

label = Label(window, text = "Length of password (6-14):")
entry = Entry(window)
btn = Button(window, text ="Generate password!", command = showPassword)
pwBox = Label(window)


#Configure & format widgets
window.config(bg = bgColor)
label.config(bg = bgColor, fg = textColor, font = avenir)
entry.config(bg = bgColor, font = avenir)
btn.config(bg = bgColor, font = avenir)
pwBox.config(bg = bgColor, font = ["Verdana", 14])
upperCaseCheckBox.config(bg = bgColor, font = avenir)
numberCheckBox.config(bg = bgColor, font = avenir)
symbolCheckBox.config(bg = bgColor, font = avenir)

#Add all to window
upperCaseCheckBox.grid(row = 0, sticky = W)
numberCheckBox.grid(row = 1, sticky = W)
symbolCheckBox.grid(row = 2, sticky = W)
label.grid(row = 3)
entry.grid(row = 3, column = 1)
btn.grid(row = 4, columnspan = 2, ipady = 5, ipadx = 5, pady = 5)

window.mainloop()
