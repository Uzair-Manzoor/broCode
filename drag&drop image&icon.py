from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)

def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)


myimage = PhotoImage(file='emojis\\misc (5).png')
#myimage1 = PhotoImage(file='emojis\\misc (7).png')

label = Label(window,image=myimage,
              #bg="#b0cbcf"
              compound='top')
label.place(x=0,y=0)
#label = Label(window,image=myimage1,
              #bg="#b0cbcf"
              #compound='left')


window.mainloop()