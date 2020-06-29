# menu bar
import tkinter
from tkinter import *
win= Tk()
menubar = Menu(win)

def func():
    print('function is working')

filemenu= Menu(menubar,tearoff=0)

filemenu.add_command(label = 'New File', command = func)
filemenu.add_command(label = 'New Window', command = func)
filemenu.add_separator()     # add seperator
filemenu.add_command(label = 'Save File', command = func)
filemenu.add_command(label = 'Exit', command = win.quit)   # quit window
menubar.add_cascade(label = 'File',menu=filemenu)    # add in main men
win.config(menu=menubar)
win.mainloop()