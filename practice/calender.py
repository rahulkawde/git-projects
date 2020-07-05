# Calender √√√√
import tkinter as tk
from tkinter import font
import calendar

win = tk.Tk()
win.title('Calender')
win.geometry('240x200')
win.resizable(0,0)

def submit():
    a= int(month_box.get())
    b= int(year_box.get())
    cal = calendar.month(b,a)

    text.delete(0.0,tk.END)
    text.insert(tk.INSERT,cal)
    

month = tk.Label(win,text = 'Month',font='helvetica 12 bold ')
month.place(x=15,y=0)

year = tk.Label(win,text = 'Year',font='helvetica 12 bold ')
year.place(x=115,y=0)

month_box = tk.Spinbox(win,values = (1,2,3,4,5,6,7,8,9,10,11,12), width = 4)
month_box.place(x=60,y=0)
year_box = tk.Spinbox(win,from_ = 1900,to_ = 2100, width = 4)
year_box.place(x=150,y=0)

submit = tk.Button(win,text='Show',command = submit)
submit.place(x=100,y=30)

text = tk.Text(win,width=30,height=8)
text.place(x=20,y=60)

win.mainloop()