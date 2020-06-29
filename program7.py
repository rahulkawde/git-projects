# use font   # msgbox
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box # for msgbox
win= tk.Tk()
win.title('PRO')

#label frame:
label_frame = ttk.LabelFrame(win,text='User Info')
label_frame.grid(row=0,column=0,padx=20,pady=10)

#label:
name_label = ttk.Label(label_frame, text ='Enter your Name :',font=('Helvetica',14))
age_label = ttk.Label(label_frame, text ='Enter your age :',font=('Helvetica',14))

#entry variable:
name_var = tk.StringVar()
age_var = tk.StringVar()

#entrybox:
name_entry =ttk.Entry(label_frame,width=16,textvariable= name_var)
age_entry =ttk.Entry(label_frame,width=16,textvariable= age_var)

#grids:
name_label.grid(row=0,column=0,padx=9,sticky =tk.W)
age_label.grid(row=0,column=1,padx=9,sticky =tk.W)
name_entry.grid(row=1,column=0,sticky =tk.W)
age_entry.grid(row=1,column=1,sticky =tk.W)

#submit:
def submit():
    # m_box.showinfo('title','why are you serious???') # show info
    # m_box.showerror('title','why are you serious???') # show error
    # m_box.showwarning('title','why are you serious???') # show warning
    name= name_var.get()
    age= age_var.get()
    if name == '' or age =='':
        m_box.showerror('Error','please input both column.')
    else:
        try:
            age= int(age)
        except ValueError:
            m_box.showerror('Error','please input number.')
        else:
            if age < 18:
                m_box.showwarning('Warning','You\'re not 18+, At Your Risk')
            print(f'{name} = {age}')            
    


submitbtm =ttk.Button(win,text='SUBMIT',command=submit)
submitbtm.grid(row=2,columnspan=2)




win.mainloop()