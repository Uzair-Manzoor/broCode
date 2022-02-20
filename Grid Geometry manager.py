from tkinter import *

# grid () = geometry manager that organizes widget in a table-like structure in a parent widget

window = Tk()

titleLabel = Label(window,text="Enter your Info",font=("Georgia",15)).grid(column=0,row=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ",width=16,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",bg="#956cad",width=16).grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emialLabel = Label(window,text="Email Address: ",bg="green",width=16).grid(row=3,column=0)
entryLabel = Entry(window).grid(row=3,column=1)

button = Button(window,text="Submit").grid(column=0,row=4,columnspan=2)
window.mainloop()