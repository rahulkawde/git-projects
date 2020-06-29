import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Tab Control')

nb= ttk.Notebook(win)    # craete Notebook
page1= ttk.Frame(nb)       # create tab
page2=ttk.Frame(nb)

nb.add(page1, text='ONE')  # add tab in notebook
nb.add(page2,text= 'TWO')

nb.pack(expand=True,fill= 'both')  # pos

label= ttk.Label(page1,text='user info')    #create label and entrybox
label.grid(row=0,column=0)
entry= ttk.Entry(page1,width=16)
entry.grid(row=0,column=1)

label2= ttk.Label(page2,text='user info2')
label2.grid(row=0,column=0)
entry2= ttk.Entry(page2,width=20)
entry2.grid(row=0,column=1)

win.mainloop()