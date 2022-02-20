# canvas = widgets that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)

#canvas.create_line(0,0,500,500,fill="violet",width=5)
#canvas.create_line(0,500,500,0,fill="purple",width=5)
#canvas.create_line(0,250,250,0,fill="red",width=5)
#canvas.create_line(250,0,250,500,fill="red",width=5)
#canvas.create_rectangle(50,50,250,250,fill="#031654")
#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill="#54032d",outline="red",width=2)
#canvas.create_arc(0,0,500,500,style=PIESLICE,fill="#050157",start=90,width=5,outline="#19fc12")
#canvas.create_arc(0,0,500,500,style=PIESLICE,fill="#91004b",start=180,width=5,outline="#19fc12")
#canvas.create_arc(0,0,500,500,style=PIESLICE,fill="#402c0a",start=360,width=5,outline="#19fc12")
#canvas.create_arc(0,0,500,500,style=PIESLICE,fill="#043602",start=270,extent=270,width=5,outline="#19fc12")
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",start=180,extent=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)
canvas.pack()

window.mainloop()