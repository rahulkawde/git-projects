from tkinter import *
win = Tk()
win.geometry('344x433')
win.title('Notepad')
win.wm_iconbitmap('Wineass-los7-Redesign-Calculator.ico')


menubar= Menu(win)
filemenu = Menu(menubar,tearoff = 0)
filemenu.add_command(label= 'File',command= None)
menubar.add_cascade(menu=filemenu, label = 'File')

win.config(menu=menubar)

#  scrollbar
text_editor = Text(win)
text_editor.config(wrap='word', relief=FLAT)

scroll_bar = Scrollbar(win)
text_editor.focus_set()
scroll_bar.pack(side=RIGHT, fill=Y)
text_editor.pack(fill=BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

win.mainloop()
