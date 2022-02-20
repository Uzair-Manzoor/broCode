from tkinter import *

def pressanyKey(event):
    #print("You pressed: "+event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",pressanyKey)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()