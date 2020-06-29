# create program and  data store in file file.txt and filepro.csv
# start code
import tkinter as tk
from tkinter import ttk        # for gui file create
from csv import DictWriter  # for csv file
win = tk.Tk()    # variable
win.title('GUI') # give title to gui

# create label:

name_label = ttk.Label(win,text='Enter Your Name:')   # title name
name_label.grid(row = 0, column = 0,sticky= tk.W)       # pos of label
email_label = ttk.Label(win,text='Enter Your Email ID:')   # title name
email_label.grid(row = 1, column = 0, sticky = tk.W)       # pos of label
age_label = ttk.Label(win,text='Enter Your Age:')   # title name
age_label.grid(row = 2, column = 0, sticky = tk.W)  # pos of label, tk.w for left side
gender_label = ttk.Label(win,text='Select Your Gender:')   # title name
gender_label.grid(row = 3, column = 0, sticky = tk.W)
# create entry box:
name_var = tk.StringVar()                                        # str for store
name_entrybox = ttk.Entry(win,width= 17, textvariable= name_var) # for box
name_entrybox.grid(row=0,column=1)                              #pos
name_entrybox.focus()                                         #focus for curser in 1st pos

email_var = tk.StringVar()                                        # str for store
email_entrybox = ttk.Entry(win,width= 17, textvariable= email_var) # for box
email_entrybox.grid(row=1,column=1)                              #pos

age_var = tk.StringVar()                                        # str for store
age_entrybox = ttk.Entry(win,width= 17, textvariable= age_var) # for box
age_entrybox.grid(row=2,column=1)                              #pos

#create combo box:
gender_var= tk.StringVar()                  #|||||||| state for dont type
gender_combobox= ttk.Combobox(win,width=16,textvariable=gender_var,state = 'readonly')             # create code
gender_combobox['values'] = ('Male','Female','Other')   #put value
gender_combobox.current(0)                           # for good look
gender_combobox.grid(row=3,column=1)                    # pos

#create radio button:
usertype = tk.StringVar()  # we use single variable for store data
rdbtn1 = tk.Radiobutton(win,text='Student',value = 'Student', variable=usertype)
rdbtn1.grid(row=4,column=0)

rdbtn2 = tk.Radiobutton(win,text='Teacher',value = 'Teacher', variable=usertype)
rdbtn2.grid(row=4,column=1)

#check button:
checkbtn_var= tk.IntVar()
checkbtn= ttk.Checkbutton(win,text= 'plz check if you agree this term', variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)

#create button    # define function for store data
# def action():
#     user_name= name_var.get()
#     user_age= age_var.get()
#     user_email= email_var.get()
#     print(f'hello {user_name},your age is{user_age} and email is {user_email}')
#     user_gender= gender_var.get()
#     user_type = usertype.get()
#     if checkbtn_var.get() == 0:
#         Agree = 'No'
#     else:
#         Agree = "Yes"    
#     print (user_gender,user_type,Agree)
#      ---------txt file-------- 
#     with open ('file.txt','a') as f:  # create file an store data
#         f.write(f'{user_name},{user_age},{user_email},{user_gender},{user_type},{Agree}\n')

#     name_entrybox.delete(0,tk.END)   # for black value
#     email_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
    
    # submit_button.configure(foreground= 'Blue')     # for colour


#write to csv files:
def action():
    user_name= name_var.get()
    user_age= age_var.get()
    user_email= email_var.get()
    user_gender= gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        Agree = 'No'
    else:
        Agree = "Yes"    
    # -------csv file--------
    with open ('filepro.csv','a',newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName','UserAge','UserEmail','UserType','UserGender','Agree'])
        dict_writer.writeheader()
        dict_writer.writerow({
            'UserName': user_name,
            'UserAge':user_age,
            'UserEmail': user_email,
            'UserType':user_type,
            'UserGender':user_gender,
            'Agree' : Agree
        })
    

    name_entrybox.delete(0,tk.END)   # for black value
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)


submit_button = ttk.Button(win,text='SUBMIT', command=action)# create button command for accept function
submit_button.grid(row=6,column=0)

win.mainloop()    # foe continue see window