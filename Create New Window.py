from tkinter import *

def create_window():
    new_window = Tk()   #Toplevel() = new window 'on top' of other window, linked to a 'bottom' window
                        #Tk() = new independent window
    old_window.destroy()    #closes the previous window

old_window = Tk()

Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop() 
