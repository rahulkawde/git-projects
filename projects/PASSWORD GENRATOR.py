# password genrator:√√√√√v  
import tkinter as tk
from tkinter import ttk
from tkinter import font
import random
import pyperclip    # copy text

win= tk.Tk()
win.geometry('300x300')
win.title('Password Genrator')

def genrator():
    passlist = ['a','b','c','d','e','f','g','h',
                'i','j','k','l','m','n','o','p','q','r','s',
                't','u','v','w','x','y','z','A','B','C','D',
                'E','F','G','H','I','J','K','L','M','N','O',
                'P','Q','R','S','T','U','V','W','X','Y','Z',
                '1','2','3','4','5','6','7','8','9','0',
                '@','#','<','>','!','$','%','^','&','(',')']
    password = ''
    for _ in range(entvar.get()):  # set value
        password = password + random.choice(passlist)
    entvar2.set(password)    

def copy():
    random_password = entvar2.get()
    pyperclip.copy(random_password)
    # print(random_password)

label1 = tk.Label(text='Password Genrator',font='helvetica 19 bold')
label1.pack()
f1 = tk.Frame(win)
f1.pack()

label2 = tk.Label(f1,text='Enter Password Length')
label2.pack()
entvar = tk.IntVar()
entvar.set(0)

entry = tk.Entry(f1, width = 16, textvariable = entvar)
entry.pack()
ttk.Button(f1,text= 'Password genrator',command=genrator).pack()

entvar2 = tk.StringVar()
entry2 = tk.Entry(f1, width = 16, textvariable = entvar2)
entry2.pack()
ttk.Button(f1,text= 'Copy Password',command=copy).pack()

win.mainloop()
