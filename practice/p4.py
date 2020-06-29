# listbox and scollbar
import tkinter 
from tkinter import *
win=Tk()
win.title('sc_lb')

# 1.widget(yscrollcommand = scollbar.set)
# 2.scollbar.config(command = widget.yview)
scrollbar= Scrollbar(win)    #create scollbar
scrollbar.pack(side=RIGHT,fill= Y)

lb= Listbox(win,yscrollcommand=scrollbar.set)     # create listbox
for i in range(500):
    lb.insert(END,f'Item no.{i}')

lb.pack(fill=BOTH,padx=20)
scrollbar.config(command=lb.yview)


win.mainloop()