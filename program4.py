# label frame: # padding in frame:
import tkinter as tk
from tkinter import ttk
from csv import DictWriter

win=tk.Tk()
win.title('Frame')

#label frame:
label_frame = ttk.LabelFrame(win,text='User Info')
label_frame.grid(row=0,column=0,padx=20,pady=10)     # use padding

# labels:  use loop:
labels = ['Enter Your Full Name :','Enter Your Age :' ,'Enter Your Gender :','country :','state :','city :','address'] 
for i in range(len(labels)):
    cur_label = 'label' + str(i) #label1,label2
    cur_label = ttk.Label(label_frame,text=labels[i]) #label_frame
    cur_label.grid(row=i,column=0,sticky = tk.W)  # add padding


#entrybox:  use loop and dict
# name_var = tk.StringVar()
user_info={
    'name': tk.StringVar(),
    'age' : tk.StringVar(),
    'gender' : tk.StringVar(),
    'country' : tk.StringVar(),
    'state' : tk.StringVar(),
    'city' : tk.StringVar(),
    'address' : tk.StringVar()
    }
counter=0    # for allign
for i in user_info:
    cur_entry= 'entry'+ i #entryname,#entryage
    cur_entrybox= ttk.Entry(label_frame,width =17,textvariable= user_info[i]) #label_frame
    cur_entrybox.grid(row=counter,column=1)
    counter +=1

# dob==============
dob_label = ttk.Label(label_frame,text='D.O.B.')
dob_label.grid(row=7,column=0,sticky = tk.W)  # add padding
date = tk.IntVar()
date_no = ttk.Combobox(label_frame,width= 10,textvariable = date)
date_no['values'] = tuple(range(1,32))
date_no.current(0)
date_no.grid(row=8,column=0,padx=4)
 
year = tk.IntVar()
year_no = ttk.Combobox(label_frame,width= 15, textvariable = year)
year_no['values'] = tuple(range(1990,2021))
year_no.current(year_no.index(2020))
year_no.grid(row=8,column=2,padx=4)

month = tk.StringVar()
month_no = ttk.Combobox(label_frame,width= 10,textvariable = month)
month_no['values'] =('JAN','FEB','MARCH','MAY','JUNE','JULY','AUG','SEP','OCT','NOV','DEC')
month_no.current(0)
month_no.grid(row=8,column=1,padx=4)


# submit button:
def action():
    print(user_info.get('name').get())   #or user_info['name'].get()
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get()) 
    print(user_info.get('address').get()) 
    print(date.get(),month.get(),year.get())

    with open('user_info.txt', 'a', newline="") as wf:
            wf.write(f'user info :{user_info.get()},{date.get(),month.get(),year.get()}\n')

       
    
submitbtm =ttk.Button(win,text='SUBMIT',command= action)
submitbtm.grid(row=2,columnspan=2)
#we addd padding in frame with help of child method
for child in label_frame.winfo_children():
    child.grid_configure(padx=4,pady=2)

win.mainloop()