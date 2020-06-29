# class in tkinter
from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x800')

    def satusbar(self,inputtext):
        self.var= StringVar()
        self.var.set('SatusBar') 
        self.satusbar = Label(self,textvariable=self.var,anchor='w')
        self.satusbar.pack(fill=X,side= BOTTOM)
    
   

    def clickbtn (self,inputtext):
        def click():
            print(inputtext) 
        Button(self,text= inputtext,command = click).pack()



win= GUI()
win.satusbar('SatusBar')

win.clickbtn('Yes')
win.clickbtn('No')
win.mainloop()
