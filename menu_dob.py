import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.geometry('1200x800')
win.title('menubar')

menu = tk.Menu(win)
files = tk.Menu(menu,tearoff = 0)
menu.add_cascade(label= 'File', menu = 'files') 


# ***************toolbar*************

tool_bar = tk.Label(win)
tool_bar.pack(fill = tk.X ,side = tk.TOP)


# dob==============
date = tk.IntVar()
date_no = ttk.Combobox(tool_bar,width= 10,textvariable = date)
date_no['values'] = tuple(range(1,32))
date_no.current(0)
date_no.grid(row=0,column=0,padx=4)
 
year = tk.IntVar()
year_no = ttk.Combobox(tool_bar,width= 15, textvariable = year)
year_no['values'] = tuple(range(1990,2021))
year_no.current(year_no.index(2020))
year_no.grid(row=0,column=2,padx=4)

month = tk.StringVar()
month_no = ttk.Combobox(tool_bar,width= 10,textvariable = month)
month_no['values'] =('JAN','FEB','MARCH','MAY','JUNE','JULY','AUG','SEP','OCT','NOV','DEC')
month_no.current(0)
month_no.grid(row=0,column=1,padx=4)










win.config(menu = menu)


win.mainloop()
