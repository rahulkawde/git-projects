#Calculator

import tkinter as tk
from tkinter import ttk
from tkinter import font


def click(event=None):
    global scalevar
    text = event.widget.cget('text')
    # print('text')
    if text == 'C':
        scalevar.set('')  # black screen
        screen.update()
        
    elif text == '=':
        if scalevar.get().isdigit():     # if type num
            value = int(scalevar.get())
        else:
            try:
                value = eval(screen.get())   # if type symbols
            except Exception as e:
                value= 'ERROR'              # show error when do any wrong
    else:
        scalevar.set(scalevar.get() + text )  # number on screen
        screen.update()

win = tk.Tk()
win.title('Calculator')
win.geometry('340x230')
win.wm_iconbitmap('Wineass-Ios7-Redesign-Calculator.ico')



scalevar = tk.StringVar()
scalevar.set('')
screen= ttk.Entry(win,textvariable = scalevar,font='helvetica 19 bold')
screen.pack(fill='x',padx= 12,pady=15)

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

f2 = ttk.Frame(win)
b= ttk.Button(f2,text='6')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f2,text='5')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f2,text='4')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f2,text='*')
b.pack(side='left',padx=5,pady=5)
b.bind('<< Button-1>>', click)
f2.pack()

f3 = ttk.Frame(win)
b= ttk.Button(f3,text='3')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f3,text='2')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f3,text='1')
b.pack(side='right',padx=5,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f3,text='/')
b.pack(side='left',padx=5,pady=5)
b.bind('<< Button-1>>', click)
f3.pack()

f4 = ttk.Frame(win)

b= ttk.Button(f4,text='.')
b.pack(side='right',padx=20,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f4,text='0')
b.pack(side='right',padx=20,pady=5)
b.bind('<< Button-1>>', click)
b= ttk.Button(f4,text='=')
b.pack(side='left',padx=20,pady=5)
b.bind('<< Button-1>>', click)
f4.pack()


win.mainloop()