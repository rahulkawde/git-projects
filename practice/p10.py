import tkinter as tk
from tkinter import ttk
from tkinter import font

win = tk.Tk()
win.title('Calculator')
win.geometry('340x230')
win.wm_iconbitmap('Wineass-Ios7-Redesign-Calculator.ico')

scalevar = tk.StringVar()
scalevar.set('0')
screen= ttk.Entry(win,textvariable = scalevar,font='helvetica 19 bold')
screen.pack(fill='x',padx= 12,pady=15)


def click (event):
    global scalevar
    text = event.widget.cget('text')
    print('text')

f_ = ttk.Frame(win)
b= ttk.Button(f_,text='C')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)

b= ttk.Button(f_,text=' ')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)

b= ttk.Button(f_,text='%')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)

b= ttk.Button(f_,text='+')
b.pack(side='left',padx=5,pady=5)
b.bind('<< Button-1>>', click)
f_.pack()

f = ttk.Frame(win)
b= ttk.Button(f,text='9')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f,text='8')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f,text='7')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f,text='-')
b.pack(side='left',padx=5,pady=5)
b.bind('<< Button-1>>', click)
f.pack()

win.mainloop()