from tkinter import *

def mouseEvents(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>",mouseEvents)   #left mouse click
#window.bind("<Button-2>",mouseEvents)  #mouse scroll wheel/button
#window.bind("<Button-3>",mouseEvents)  #left mouse click
#window.bind("<ButtonRelease>",mouseEvents)
#window.bind("<Enter>",mouseEvents)     #enter the window
#window.bind("<Leave>",mouseEvents)     #leave the window
#window.bind("<Motion>", mouseEvents)    #Where the mouse moved

window.mainloop()