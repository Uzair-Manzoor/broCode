# listbox = A listing of selectable text items within it own container

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    #print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)

def Add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def Delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

from  tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#9acc93",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE)

listbox.pack()

listbox.insert(1,"Chicken Pizza")
listbox.insert(2,"Italian Pasta")
listbox.insert(3,"Zinger Burger")
listbox.insert(4,"Corn Soup")
listbox.insert(5,"Russian Salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="Submit",command=submit)
submitButton.pack()

addButton = Button(window,text="Add",command=Add)
addButton.pack()

deleteButton = Button(window,text="Delete",command=Delete)
deleteButton.pack()

window.mainloop()