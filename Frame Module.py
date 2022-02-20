# Frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="#57667d",bd=3,relief=SUNKEN)
frame.place(x=100,y=100)

Button(frame,text="S",font=("Georgia",25),width=3,bg="#995767").pack(side=TOP)
Button(frame,text="A",font=("Georgia",25),width=3,bg="#db0bb9").pack(side=LEFT)
Button(frame,text="M",font=("Georgia",25),width=3,bg="#b82a38").pack(side=LEFT)
Button(frame,text="I",font=("Georgia",25),width=3,bg="#338182").pack(side=LEFT)

window.mainloop()

