import tkinter 
from tkinter import *
import tkinter.messagebox as mbox
win= Tk()
win.geometry('500x400')
win.title('Rating Us')
def fuc():
    print(f'you rate us{s1.get()}')
    mbox.showinfo('ABC','Thank you!!!')

Label(win,text='Please Rate Us!!',font='helvatica 19 bold').pack()
s1=Scale(win,from_ =0, to=10, orient='horizontal')
s1.pack()

Button(win,text = 'Submit',command=fuc).pack()
win.mainloop()
