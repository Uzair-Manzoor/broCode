from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\CP\\PycharmProjects\\python fun begins",
                                          title="Open file PLEASE For GOD Sake",
                                          filetypes=(("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="open",command=openfile)
button.pack()

window.mainloop()