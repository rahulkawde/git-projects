
# window Resizer

from tkinter import *
win = Tk()
win.geometry('300x300')

def submit():
    n_width = width_var.get()
    n_height = height_var.get()
    win.geometry(f'{n_width}x{n_height}')  # chnge geometry
    # print(f'{n_width} x {n_height}')

win.title('Resizer')


# label = Label(win, text= 'Resizer',font='helvetica 30 bold').grid()

l1= Label(win,text='Width :',font='helvetica 19 bold')
l2= Label(win,text ='Height :',font='helvetica 19 bold')

width_var = StringVar()
height_var = StringVar()

e1= Entry(win,width= 10,textvariable= width_var)
e2= Entry(win,width= 10,textvariable= height_var)

l1.grid(row=0,column=0,padx=5,pady=5,sticky= W)
l2.grid(row=1,column=0,padx=5,pady=5,sticky= W)
e1.grid(row=0,column=1,padx=5,pady=5,sticky= W)
e2.grid(row=1,column=1,padx=5,pady=5,sticky= W)

Button(win,text='Submit',command=submit).grid(row=2,columnspan=2,padx=5,pady=5)

win.mainloop()