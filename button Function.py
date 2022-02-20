from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count+=1
    print(count)
    print("You clicked the button!")


window = Tk()

photo = PhotoImage(file='pngfile.png')

button = Button(window,
                text="Click Here!",
                command=click,
                font=("Comic Sans",30,'bold'),
                fg="#00FF00",
                bg="black",
                activebackground="black",
                activeforeground="violet",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()



window.mainloop()