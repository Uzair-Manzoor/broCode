from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("600x510")
window.title("Uzair's first GUI program")

icon = PhotoImage(file='abdulaziz.png')
window.iconphoto(True,icon)
window.config(background="#5f98b0")
photo = PhotoImage(file='pngfile.png')
label = Label(window,
              text="ABDUL AZIZ",
              font=('Georgia',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady= 20,
              image=photo,
              compound='bottom')
label.pack()
#label.place(x=100,y=100)

window.mainloop() #place window on computer screen, listen for events
