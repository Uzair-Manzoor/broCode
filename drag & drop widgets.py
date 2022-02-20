from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

window = Tk()

window.geometry("500x500")
window.title("Drag and Drip widgets in a window")

label = Label(window,text="Abdul Aziz",font=("Georgia"),bg="#8c0606",width=20,height=10)
label.place(x=0,y=0)

label1 = Label(window,bg="#0c068c",width=20,height=10)
label1.place(x=100,y=100)

label2 = Label(window,bg="#055c04",width=20,height=10)
label2.place(x=200,y=200)

label3 = Label(window,bg="#7d0909",width=20,height=10)
label3.place(x=300,y=300)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label1.bind("<Button-1>",drag_start)
label1.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

label3.bind("<Button-1>",drag_start)
label3.bind("<B1-Motion>",drag_motion)

window.mainloop()