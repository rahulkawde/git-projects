# pending  log in
import tkinter as tk 
from tkinter import ttk
from tkinter import font
from csv import DictReader,DictWriter
from tkinter import messagebox as mbox

win = tk.Tk()
win.title('Log in')
win.geometry('320x231')
#functions *****************************
def login():
    # username = username_var.get()
    # password = pass_var.get()
    with open('userInfo1.txt') as rf:
        for line in rf.readlines():
            if usernames_var.get() == '' or password_var.get() == '' :
                mbox.showerror('Error','Please input all information !!!')
            elif usernames_var.get() != 'rahul'  or password_var.get() != '123' :
                mbox.showerror('Error','Please input all information !!!')  
            else:
                mbox.showinfo('Login','welcome \n LogIn success')
                    
        
def signup():


    def submit():
        name = name_var.get()
        user = username_var.get()
        passw = pass_var.get()
        dob = dob_var.get()

        if name == '' or user == '' or passw == '' or dob == '' :
            mbox.askretrycancel('Error','please input all information !!!')

        else:
            with open('userInfo1.txt','a') as wf:
                files = wf.writelines(f'{name_var.get()},{username_var.get()},{pass_var.get()},{dob_var.get()} \n ')
                print(pass_var.get())
                # tk.Label(text= 'successfull', bg = 'green')
                screen.destroy()
       

    screen = tk.Toplevel(win)
    screen.title('Sign Up')
    screen.geometry('320x331')

    label4 = tk.Label(screen,text='Please Sign Up',font = 'calibri 20 bold')
    label4.pack()
    
    label5 = tk.Label(screen,text='Please Enter Your Full Name :',font = 'calibri 15 ')
    label5.pack()
    name_var = tk.StringVar()
    entry3 = tk.Entry(screen,width = 15, textvariable = name_var)
    entry3.pack()

    label6 = tk.Label(screen,text='Enter Your Username :',font = 'calibri 15 ')
    label6.pack()
    username_var = tk.StringVar()
    entry4 = tk.Entry(screen,width = 15, textvariable = username_var)
    entry4.pack()

    label7 = tk.Label(screen,text='Enter Your Date of Birth : ',font = 'calibri 15 ')
    label7.pack()
    dob_var = tk.StringVar()
    entry5 = tk.Entry(screen,width = 15, textvariable = dob_var)
    entry5.pack()

    label8 = tk.Label(screen,text='Enter Your Password :',font = 'calibri 15 ')
    label8.pack()
    pass_var = tk.StringVar()
    entry6 = tk.Entry(screen,width = 15, textvariable = pass_var)
    entry6.pack()

    submitbtn = ttk.Button(screen,text = 'Submit',command = submit)
    submitbtn.pack()





# main log in window********************
label1 = tk.Label(win,text= 'Please Sign In Below ', font = 'helvetica 20 bold')
label1.pack()
label2 = tk.Label(win,text= 'Username: ', font = 'helvetica 15 ')
label2.pack()
usernames_var = tk.StringVar()
entry1 = tk.Entry(win, width=15,textvariable = usernames_var)
entry1.pack()
label3 = tk.Label(win,text= 'Password: ', font = 'helvetica 15 ')
label3.pack()
password_var = tk.StringVar()
entry2 = tk.Entry(win, width=15,textvariable = password_var)
entry2.pack()
loginbtn = ttk.Button(text= 'Log In',command= login)
loginbtn.pack()
label9 = tk.Label(win,text='Click Here for SignUp : ',font = 'calibri 15 ')
label9.pack()
signupbtn = ttk.Button(text= 'Sign Up',command= signup)
signupbtn.pack()
win.mainloop()