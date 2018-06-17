from tkinter import *
import string
from random import *

smallFont = ["Courier", 14]
avenir = ["Avenir", 14]
bgColor = "#F9EEF5"
textColor = "#000000"
password = ""
#button function that occurs when button is pressed
def showPassword():
    c2c.grid_forget()
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
        global password
        password = generatePassword(length)
        pwBox.configure(text = "Generated password: " + password)
        c2c.grid(row = 6, columnspan = 2, ipady = 5, ipadx = 5)
    except ValueError:
        pwBox.configure(text = "Input has to be a number")
        entry.delete(0,END)
    pwBox.grid(row = 5, columnspan = 2, ipady = 10)

#Copy to clipboard method
def copyToClipboard():
    window.clipboard_clear()
    window.clipboard_append(password)
    print(window.clipboard_get())
    c2c.configure(text="Copied!")

#Generate the password of given length
def generatePassword(length):
    wordLength = length
    if number.get() == 1: wordLength -= 1
    if symbol.get() == 1: wordLength -= 1

    try:
        with open ("words.txt", "r") as file: #Open text file
            words = set(file.read().split())
            words1 = []
            for word in words: #Find words of specific length and put it into a list
                if len(word) == wordLength:
                    words1.append(word)
            password = choice(words1) #Get random word from list of words
            if upperCase.get() == 1:
                password = password.title() #Capitalise
            if number.get() == 1:
                password += str(choice(string.digits)) #Add number
            if symbol.get() == 1:
                password += str(choice(string.punctuation)) #Add symbol
            return shuffleWord(password) #Shuffle string
    except IOError:
        return "FILE LOAD ERROR"

#Mix up characters in string
def shuffleWord(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

#Create GUI for a window
window = Tk()
window.geometry("400x300")
window.resizable(0,0)
window.grid_propagate(0)
window.title("Password generator")

upperCase = IntVar(value = 1)
upperCaseCheckBox = Checkbutton(window, text = "UpperCase letter", variable = upperCase)
number = IntVar(value = 1)
numberCheckBox = Checkbutton(window, text = "Number: 1234567890", variable = number)
symbol = IntVar(value = 1)
symbolCheckBox = Checkbutton(window, text = "Symbol: !@#$%^&*()", variable = symbol)

label = Label(window, text = "Length of password (6-14):")
entry = Entry(window)
btn = Button(window, text ="Generate password!", command = showPassword)
pwBox = Label(window)
c2c = Button(window, text ="Copy to clipboard", command = copyToClipboard)

#Configure & format widgets
window.config(bg = bgColor)
label.config(bg = bgColor, fg = textColor, font = avenir)
entry.config(bg = bgColor, font = avenir)
btn.config(bg = bgColor, font = avenir)
pwBox.config(bg = bgColor, font = ["Verdana", 14])
upperCaseCheckBox.config(bg = bgColor, font = avenir)
numberCheckBox.config(bg = bgColor, font = avenir)
symbolCheckBox.config(bg = bgColor, font = avenir)
c2c.config(bg = bgColor, font = avenir)

#Add all to window
upperCaseCheckBox.grid(row = 0, sticky = W)
numberCheckBox.grid(row = 1, sticky = W)
symbolCheckBox.grid(row = 2, sticky = W)
label.grid(row = 3)
entry.grid(row = 3, column = 1)
btn.grid(row = 4, columnspan = 2, ipady = 5, ipadx = 5, pady = 5)

window.mainloop()
