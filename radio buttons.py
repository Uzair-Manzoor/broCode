# radio buttons = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["Pizza","Hamburger","Hotdog"]

def order():
    if(x.get()==0):
        print("You ordered Pizza!")
    elif(x.get()==1):
        print("You ordered Hamburger!")
    elif(x.get()==2):
        print("You ordered Hotdog!")
    else:
        print("huh?")

window = Tk()

pizzaImage = PhotoImage(file="emojis\\png (8).png")
hamburgerImage = PhotoImage(file="emojis\\png (21).png")
hotdogImage = PhotoImage(file="emojis\\png (1).png")
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                               text=food[index], # adds text to the radio buttons
                               variable=x, # groups radiobuttons together if they share same variable
                               value=index, # assigns each radiobutton a different value
                               padx = 25, # adds padding on x-axis
                               font=("Georgia",50),
                               image = foodImages[index],
                              compound = 'left',
                              indicatoron=0,
                              width = 575,
                              command=order
                               )
    radiobutton.pack(anchor=W)

window.mainloop()