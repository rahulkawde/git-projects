#stopwatch 
import tkinter as tk
from tkinter import ttk
from tkinter import font


global count
count = 0 

class stopwatch():
# start function
    def start(self):
        global count
        count = 0 
        self.start_timer()

    def start_timer(self):
        global count
        self.timer()    

# stop function
    def stop(self):
        global count
        count=1
# reset function
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')

# timer function:        
    def timer(self):
        global count
        if count == 0:
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(':'))

            # h = int(h)
            # m = int(m)
            # s = int(s)

            if (s < 59):
                s+=1
            elif s == 59:
                s==0
                if m < 59:
                    m+=1    
                elif m==59:
                    h+=1
            if h < 10:               # for 01:01:01
                h = str(0)+str(h)
            else:
                h = str(h) 
            if m < 10:
                m = str(0)+str(m)
            else:
                m = str(m) 
            if s < 10:
                s = str(0)+str(h)
            else:
                s = str(s)      
            self.d = h+':'+m+':'+s                  
            
            self.t.set(self.d)
            if count==0:
                self.win.after(930,self.start_timer)


    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Stopwatch')
        self.win.geometry('330x150')
        # self.win.resizable(0,0)
        self.t = tk.StringVar()
        self.t.set('00:00:00')
        self.lb = tk.Label(self.win,textvariable = self.t,font='helvetica 80 bold')
        self.lb.grid(row=0,columnspan=3)
        self.b1 = ttk.Button(self.win,text = 'Start',command = self.start)
        self.b1.grid(row=1,column=0)
        self.b2 = ttk.Button(self.win,text = 'Stop',command = self.stop)
        self.b2.grid(row=1,column=1)
        self.b3 = ttk.Button(self.win,text = 'Reset',command = self.reset)
        self.b3.grid(row=1,column=2)

        self.win.mainloop()


stopwatch()

