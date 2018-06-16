from tkinter import *
import string
from random import *

smallFont = ["Courier", 14]
mediumFont = ["Avenir", 16]
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
        pwBox.pack()


#Create GUI for a window
window = Tk()
window.geometry("400x400")
window.resizable(0,0)
window.pack_propagate(0)

window.title("Password generator")
label = Label(window, text = "Length of password:")
entry = Entry(window)
btn = Button(window, text ="Generate", command = showPassword)
pwBox = Label(window)



#Configure & format widgets
window.config(bg = bgColor)
label.config(bg = bgColor, fg = textColor, font = smallFont)
entry.config(bg = bgColor, font = smallFont)
btn.config(bg = bgColor, font = smallFont)
pwBox.config(bg = bgColor, font = smallFont)

#Add all to window
label.pack(ipady = 5)
entry.pack()
btn.pack(ipady = 5, ipadx = 5, pady = 5)

window.mainloop()
