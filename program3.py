# create label and entry box with help of looping # padding
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('INFO')
# labels:  use loop:
labels = ['Enter Your Full Name :','Enter Your Age :' ,'Enter Your Gender :','country :','state :','city :','address'] 
for i in range(len(labels)):
    cur_label = 'label' + str(i) #label1,label2
    cur_label = ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky = tk.W,padx =10)  # add padding


#entrybox:  use loop and dict
name_var = tk.StringVar()
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
    cur_entrybox= ttk.Entry(win,width =17,textvariable= user_info[i])
    cur_entrybox.grid(row=counter,column=1,padx = 10,)
    counter +=1




 
 #check button:
# checkbtn_var= tk.IntVar()
# checkbtn = tk.Checkbutton(win,text='check if you Agree term *', variable = checkbtn_var)
# checkbtn.grid(row=9,column=0) 

# submit button:
def action():
    print(user_info.get('name').get())   #or user_info['name'].get()
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get()) 
    print(user_info.get('address').get()) 

   
    
submitbtm =ttk.Button(win,text='SUBMIT',command= action)
submitbtm.grid(row=10,column=1)


win.mainloop()