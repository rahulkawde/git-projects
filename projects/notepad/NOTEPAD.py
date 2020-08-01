# NotePad BY RK √

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox 
import os

win = tk.Tk()
win.title('Untitle-NotePad')

#************functions************************
#************File function********************
url = ''
def new_file(event= None):
    global url                              # for chnge value of url
    url = ''                                # chnge value  
    text_editor.delete(1.0 ,tk.END)         # using delete delete all text on texteditor
    

def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'SELECT FILES', filetypes = (('text file','.txt'),('All file','*.*')))
    try:                                        #||||     OPEN file box and selct file  |||||
        with open (url , 'r') as rf:             #for open file and read
            text_editor.delete(1.0 , tk.END)        # delete previous data
            text_editor.insert(1.0, rf.read() )     # add new file data
    except FileNotFoundError:                       # for file not found error 
        return
    win.title(os.path.basename(url))    # for rename 


def save_file(event=None):
    global url 
    try:    # for blank file
        if url :
            content = str(text_editor.get(1.0 , tk.END))    # get content on file
            with open(url ,'w', encoding='utf-8') as wf:        # open file and write data
                wf.write(content)                               # wite data in url to content
        else:  # when you write content in your file
            url = filedialog.asksaveasfile(mode='w',defaultextension = '.txt',filetypes=(('text','.txt'),('All files','*.*'))) 
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return


def save_as(event=None):
    global url 
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return 

def exit_file():
    global url, text_changed
    try :
        if text_changed :
            mbox = messagebox.askyesnocancel('Warring','Do you want to Save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open (url,'w',encoding= 'utf-8') as wf:        # get data n write
                        wf.write(content)     #store 
                        win.destroy()     # exit main window
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode= 'w', defaultextension= '.txt',files = (('text','.txt'),('All files','*.*')))
                    url.write(content2)
                    url.close()
                    win.destroy()
            elif mbox is False:
                win.destroy()
        else :
            win.destroy()
    except:
        return            



#************Edit function********************√√√√√√√√√√√√√√√√
def find_func(event= None): # find and replace term
    def find():
        word = entry_find.get()    # get info in entry box
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos=end_pos
                text_editor.tag_config('match', foreground= 'red',background='yellow')

    def replace():
        word = entry_find.get()  # get info in entry box
        replace = entry_replace.get()  # get info in entry box
        content = text_editor.get(1.0,tk.END)   # get info in text editor
        new_content = content.replace(word,replace)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0, new_content)
    
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250')
    find_dialogue.title('Find and Replace')
    find_dialogue.resizable(0,0)

    f1= tk.LabelFrame(find_dialogue,text= 'Find/Replace')
    f1.pack(pady =20)

    find_label = ttk.Label(f1,text = 'Find : ')
    replace_label = ttk.Label(f1,text = 'Replace : ')
    find_label.grid(row=0,column=0,padx=10,pady=10)
    replace_label.grid(row=1,column=0,padx=10,pady=10)

    entry_find = ttk.Entry(f1,width= 20)
    entry_replace = ttk.Entry(f1,width= 20)
    entry_find.grid(row=0,column=1,padx=10,pady=10)
    entry_replace.grid(row=1,column=1,padx=10,pady=10)

    find_btn = ttk.Button(f1,text='FIND',command= find)
    replace_btn = ttk.Button(f1,text='REPLACE',command = replace)
    find_btn.grid(row=2,column=0,padx=10,pady=10)
    replace_btn.grid(row=2,column=1,padx=10,pady=10)

    find_dialogue.mainloop()







#***********************text editor **********
text_editor = tk.Text(win)
text_editor.config(wrap = 'word', relief = tk.FLAT)

scroll_bar = tk.Scrollbar(win)      # create scroll bar
text_editor.focus()                 # cursor on text editor
scroll_bar.pack(fill= tk.Y,side= tk.RIGHT) # scroll bar pack
text_editor.pack(fill = tk.BOTH, expand = True) # text editor pack
scroll_bar.config(command= text_editor.yview)  # scrollbar add in textbar
text_editor.config(yscrollcommand= scroll_bar.set) # texteditor link scrollbar

# **********************mainmenu***************
mainmenu = tk.Menu()
#***********************exitmenu***************

# **********************filemenu***************

file_menu = tk.Menu(mainmenu,tearoff= False)
file_menu.add_command(label= 'New',compound = tk.LEFT,accelerator= 'ctrl+N', command = new_file)
file_menu.add_command(label= 'Open', compound = tk.LEFT,accelerator= 'ctrl+O', command = open_file)
file_menu.add_separator()
file_menu.add_command(label= 'Save', compound = tk.LEFT,accelerator= 'ctrl+S', command = save_file)
file_menu.add_command(label= 'Save as', compound = tk.LEFT, command = save_as)
file_menu.add_separator()
file_menu.add_command(label= 'Exit', compound = tk.LEFT,accelerator= 'ctrl+Q', command = exit_file)
mainmenu.add_cascade(label = 'File', menu = file_menu)
#***********************exitmenu***************

# **********************editmenu***************

edit_menu = tk.Menu(mainmenu,tearoff= False)                                            # event genrate and set command
edit_menu.add_command(label= 'Copy', compound = tk.LEFT,accelerator= 'ctrl+C', command = lambda: text_editor.event_generate ('<Control + c>'))
edit_menu.add_command(label= 'Cut' ,compound = tk.LEFT,accelerator= 'ctrl+X', command = lambda: text_editor.event_generate ('<Control + x>'))
edit_menu.add_command(label= 'Paste', compound = tk.LEFT,accelerator= 'ctrl+V', command = lambda: text_editor.event_generate ('<Control + v>'))
edit_menu.add_separator()
edit_menu.add_command(label= 'Find', compound = tk.LEFT,accelerator= 'ctrl+F', command = find_func)
mainmenu.add_cascade(label = 'Edit', menu = edit_menu)

#***********************exitmenu***************
# **********************viewmenu***************
statusbar_var = tk.BooleanVar()
statusbar_var.set(True)

def hide_statusbar():
    global statusbar_var
    if statusbar_var:
        status_bar.pack_forget()  # for hide
        statusbar_var=False
    else:
        status_bar.pack(side=tk.BOTTOM)    
        statusbar_var= True

view_menu = tk.Menu(mainmenu,tearoff= False)
view_menu.add_checkbutton(label ='Status Bar', onvalue= 1,offvalue=False,variable=statusbar_var,compound=tk.LEFT,command=hide_statusbar)
mainmenu.add_cascade(label = 'View', menu = view_menu)

#***********************exitmenu***********
# **********************helpmenu***************

help_menu = tk.Menu(mainmenu,tearoff= False)
help_menu.add_command(label= 'About', compound = tk.LEFT)
mainmenu.add_cascade(label = 'Help', menu = help_menu)

#***********************exitmenu***************


win.config(menu=mainmenu)   # for show main menu

##############################################  status bar ###################################################

status_bar = ttk.Label(win, text = 'Status Bar')
status_bar.pack(side=tk.BOTTOM)    # attch status bar

text_changed = False            # 
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True 
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)


# -------------------------------------&&&&&&&& End  status bar &&&&&&&&&&& ----------------------------------

#********************assing shortcuts**************
win.bind("<Control-n>", new_file)
win.bind("<Control-o>", open_file)
win.bind("<Control-s>", save_file)
win.bind("<Control-q>", exit_file)
win.bind("<Control-f>", find_func)

win.mainloop()