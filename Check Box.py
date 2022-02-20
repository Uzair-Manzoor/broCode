
from tkinter import *

def display():
    if(x.get()):
        print("You agree!")
    else:
        print("You didn't agree : ( ")

window = Tk()

x = BooleanVar()

photo = PhotoImage(file='apple-touch-icon.png')
check_button = Checkbutton(window,
                           text='You Agree To Something',
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Georgia',48),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')

check_button.pack()
window.mainloop()
