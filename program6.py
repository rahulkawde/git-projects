# MenuBar
import tkinter as tk
from tkinter import ttk
win= tk.Tk()
win.title('Menubar')

def func():
    print('function is working')

# menu bar
main_menu = tk.Menu(win)    # menubar
file_menu = tk.Menu(main_menu,tearoff =0)# 1st menu
file_menu.add_command(label = 'New File', command = func)
file_menu.add_command(label = 'New Window', command = func)
file_menu.add_separator()     # add seperator
file_menu.add_command(label = 'Save File', command = func)
file_menu.add_command(label = 'Exit', command = win.quit)   # quit window
main_menu.add_cascade(label = 'File',menu=file_menu)    # add in main menu
 
edit_menu = tk.Menu(main_menu,tearoff =0)# 2st menu
edit_menu.add_command(label = 'Undo', command = func)
edit_menu.add_command(label = 'Redo', command = func)
edit_menu.add_separator()     # add seperator
edit_menu.add_command(label = 'Copy', command = func)
edit_menu.add_command(label = 'Paste', command = func)
edit_menu.add_command(label = 'Cut', command = func)
main_menu.add_cascade(label = 'Edit',menu=edit_menu) # add 2nd menu in main menu

win.config(menu = main_menu)


win.mainloop()