import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('NotePad')
win.geometry('1200x900')
win.minsize(900,600)
#frame
f1= ttk.Frame(win)
f1.pack(side=tk.TOP,fill=tk.X,pady=5,padx=10)
l1= ttk.Label(f1,text ='label1',font='helvetica 19 bold')
l1.grid(row=0,column=0)

f2= ttk.Frame(win)
f2.pack(side=tk.LEFT,fill=tk.Y,padx=10,pady=5)
l2= ttk.Label(f2,text ='label2',font='helvetica 19 bold')
l2.grid(row=1,column=0,padx=10,pady=10)

win.mainloop()