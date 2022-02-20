from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,3,1,"#d43024")
tennis_ball = Ball(canvas,0,0,50,6,5,"#133d2c")
basket_ball = Ball(canvas,0,0,125,8,7,"#09426e")
scotch_ball = Ball(canvas,0,150,75,3,2,"#5c084f")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    scotch_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
