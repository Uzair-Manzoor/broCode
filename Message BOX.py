from tkinter import *
from tkinter import messagebox # import messagebox liberary

def click():
    #messagebox.showinfo(title='This is an info message box', message='You are wonderful!')
    #while(True):
        #messagebox.showwarning(title='WARNING!', message='You are a VIRUS')
    #messagebox.showerror(title='ERROR',message='Something went wrong : (')
    #if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing?'):
        #print('You did a thing')
    #else:
        #print('You canceled a thing!')
    #if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry the thing?'):
        #print('You retried the thing!')
    #else:
        #print('You canceled a thing!')
    #if messagebox.askyesno(title='ask yes or no',message= 'Do you like cake?'):
        #print('I Like cake too!!! :)')
    #else:
        #print('Why dont you like the cake thats weird.. EWWw')
    #answer = messagebox.askquestion(title='ask question',message='Do you like Pie??')
    #if(answer == 'yes'):
        #print('I like pie too :)')
    #else:
        #print('Go F*c* your self!! :D')

    answer = messagebox.askyesnocancel(title='yes no cancel',message='Do you like to code?',icon='info')
    if (answer==True):
        print("You like to code!! :DD")
    elif(answer==False):
        print("Then why are you watching a video on coding??")
    else:
        print("You have dodged the question!")


window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()