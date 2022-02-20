from tkinter import *

def button_press(num):

    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():

    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

def clear():

    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()

window.title("Calculator")
window.geometry("450x450")
equation_text = ""

equation_label = StringVar ()
label = Label(window,textvariable=equation_label, font=('consolas',20),bg='#f7e6e9',width=24,height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35,
                 command=lambda: button_press(1))
button1.grid(column=0,row=0)

button2 = Button(frame,text=2,height=4,width=9,font=35,
                 command=lambda: button_press(2))
button2.grid(column=1,row=0)

button3 = Button(frame,text=3,height=4,width=9,font=35,
                 command=lambda: button_press(3))
button3.grid(column=2,row=0)

button4 = Button(frame,text=4,height=4,width=9,font=35,
                 command=lambda: button_press(4))
button4.grid(column=0,row=1)

button5 = Button(frame,text=5,height=4,width=9,font=35,
                 command=lambda: button_press(5))
button5.grid(column=1,row=1)

button6 = Button(frame,text=6,height=4,width=9,font=35,
                 command=lambda: button_press(6))
button6.grid(column=2,row=1)

button7 = Button(frame,text=7,height=4,width=9,font=35,
                 command=lambda: button_press(7))
button7.grid(column=0,row=2)

button8 = Button(frame,text=8,height=4,width=9,font=35,
                 command=lambda: button_press(8))
button8.grid(column=1,row=2)

button9 = Button(frame,text=9,height=4,width=9,font=35,
                 command=lambda: button_press(9))
button9.grid(column=2,row=2)

button0 = Button(frame,text=0,height=4,width=9,font=35,
                 command=lambda: button_press(0))
button0.grid(column=1,row=3)

plus = Button(frame,text='+',height=4,width=9,font=35,
                  command=lambda: button_press('+'))
plus.grid(column=3,row=0)

minus = Button(frame,text='-',height=4,width=9,font=35,
                  command=lambda: button_press('-'))
minus.grid(column=3,row=1)

multiply = Button(frame,text='*',height=4,width=9,font=35,
                  command=lambda: button_press('*'))
multiply.grid(column=3,row=2)

divide = Button(frame,text='/',height=4,width=9,font=35,
                  command=lambda: button_press('/'))
divide.grid(column=3,row=3)

equal = Button(frame,text='=',height=4,width=9,font=35,
                  command=equals)
equal.grid(column=2,row=3)

decimal = Button(frame,text='.',height=4,width=9,font=35,
                  command=lambda: button_press('.'))
decimal.grid(column=0,row=3)

clear = Button(window,text='clear the shit outa screen',height=1,width=35,font=35,bg="#07b091",
                  command=clear)
clear.pack()

window.mainloop()

