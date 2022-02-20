from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+ " degrees C")

window = Tk()

hotImage = PhotoImage(file='emojis\\png (201).png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=250,
              orient=VERTICAL, #orientation of scale
              font = ('Concolas',15),
              tickinterval = 10, #adds numeric indicatirs for value
              #showvalue = 0, #hide current value
              resolution = 5,
              troughcolor = '#69AEFF',
              fg = '#FF1C00',
              bg = '#111111'
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) # set current value for slider

scale.pack()

coldImage = PhotoImage(file='emojis\\png (123).png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()