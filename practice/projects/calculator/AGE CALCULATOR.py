# AGE CALCULATOR :

from tkinter import *
from datetime import date
from tkinter import messagebox


win = Tk()
win.geometry('250x321')
win.minsize(250,321)
win.title('Age Calculator')


photo = PhotoImage(file='practice/projects/calculator/1n.png')
myimg = Label(image=photo)
myimg.grid (row=0,column=1)

def agecalculate():
    today= date.today()
    birthDate= date(int(yearEntry.get()),
    int(monthEntry.get()),int(dayEntry.get()))
    age= today.year - birthDate.year -((today.month,today.day) < (birthDate.month,birthDate.day))
    Label(text=f'{nameValue.get()} Your Age Is {age}').grid(row=6,column=1)
    

        
Label(text='Name : ', font = 'helvetica 19 bold').grid(row=1,column=0,padx=4)
Label(text='Year : ', font = 'helvetica  19 bold').grid(row=2,column=0,padx=4)
Label(text='Month : ', font = 'helvetica 19 bold').grid(row=3,column=0,padx=4)
Label(text='Day : ', font = 'helvetica 19 bold').grid(row=4,column=0,padx=4)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(win,width=16,textvariable = nameValue)
yearEntry = Entry(win,width=16,textvariable = yearValue)
monthEntry = Entry(win,width=16,textvariable = monthValue)
dayEntry = Entry(win,width=16,textvariable = dayValue)

nameEntry.grid(row=1,column=1,padx=5,pady=5)
yearEntry.grid(row=2,column=1,padx=5,pady=5)
monthEntry.grid(row=3,column=1,padx=5,pady=5)
dayEntry.grid(row=4,column=1,padx=5,pady=5)

Button(text='Calculate Age',font = 'helvetica 10 bold', command= agecalculate).grid(row=5,column=1,padx=5,pady=5)


win.mainloop()