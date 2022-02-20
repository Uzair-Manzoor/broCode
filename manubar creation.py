from tkinter import *

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")
def cut():
    print("You cut the file!")
def paste():
    print("File has been pasted")
def copy():
    print("file has been copied")

window = Tk()

openImage = PhotoImage(file="C:\\Users\\CP\PycharmProjects\\python fun begins\\emojis\\png (198).png")
saveImage = PhotoImage(file="C:\\Users\\CP\\PycharmProjects\\python fun begins\\emojis\\png (191).png")
exitImage = PhotoImage(file="C:\\Users\\CP\\PycharmProjects\\python fun begins\\emojis\\png (182).png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("Arial",10))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')

editMenu = Menu(menubar,tearoff=0,font=("Arial",10))
menubar.add_cascade(label= "Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()