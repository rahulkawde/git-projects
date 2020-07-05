# Paint               save function not working
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser,filedialog,messagebox
from PIL import ImageGrab

win = tk.Tk()
win.title('Paint')
win.wm_iconbitmap('practice/paint.ico')
win.geometry('800x570')
win.resizable(0,0)
#************************* variable ************
pen_colour ='black'
eraser_colour = 'white'
#***********************************************
#************************* functions ***********
def button():
    print(colour)

def select_colour(col):
    global pen_colour
    pen_colour = col

def eraser ():
    global pen_colour
    pen_colour = eraser_colour

def convas_colour():  
    global eraser_colour
    color = colorchooser.askcolor()
    canvas.configure(background = color[1])
    eraser_colour = color[1]

def more():
    global pen_colour
    more_colour = colorchooser.askcolor()
    pen_colour = more_colour[1]

def save_image():
    try:
        filename = filedialog.asksaveasfilename(defaultextension = '.jpg')
        # print(filename)
        x = win.winfo_rootx()+ canvas.winfo_x()
        # print(x,canvas.winfo_x())
        y = win.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
        messagebox.showinfo('Save Image','Image saved'+ (filenamse))
    except:
        messagebox.showerror('Error','Something get wrong !!')   
#***********************************************
#*********************colour********************
Frame=LabelFrame(win,text='Colour', font = 'Arial 14 bold',background = 'white',bd = 5,relief = RIDGE)
Frame.place(x=0,y=0,width = 80,height =156)

colours = ['#ff5733','#ffffff','#000000','#fffb00','#0004ff','#00ff13','#f300ff','#00fbff','#7a7a7a','#851087','#c4286f','#108741']

i=j=0
for colour in colours:
    Button(Frame,background=colour,bd=5,relief=RIDGE,width = 4,command = lambda col=colour : select_colour(col)).grid(row=i,column=j)
    i+=1
    if i==6:
        i=0
        j=1

more_colour = ttk.Button(win,text='Colour',command= more)
more_colour.place(x=0,y=158,width=80,height=30)

eraser_button = ttk.Button(win,text='Eraser',command= eraser)
eraser_button.place(x=0,y=188,width=80,height=30)

clear_button = ttk.Button(win,text='Clear',command= lambda : canvas.delete('all'))
clear_button.place(x=0,y=218,width=80,height=30)

save_button = ttk.Button(win,text='Save',command=save_image)
save_button.place(x=0,y=248,width=80,height=30)

canvas_button = ttk.Button(win,text='Canvas',command=convas_colour)
canvas_button.place(x=0,y=278,width=80,height=30)
# font='Arial 14 bold',width=3,bd=5,relief = RIDGE,
#***********************************************
# ************************* pen size *******************
size_frame = LabelFrame(win,text='Size',font='Arial 20 bold',bd=5,bg = 'white',relief=RIDGE)
size_frame.place(x=0,y=308,width=80,height=260)
size = ttk.Scale(size_frame,orient= VERTICAL,from_ = 50 ,to =0, length = 170)
size.set(1)
size.grid(row=0,column =1,padx=15) 
# **************************************************
#**************************canvas*******************
canvas = Canvas(win,bg='white',bd=5,relief=RIDGE,height=550,width=700)
canvas.place(x=80,y=0)

def paint(event):
    x1,y1 =(event.x-2),(event.y-2)
    x2,y2 =(event.x+2),(event.y+2)

    canvas.create_oval(x1,y1,x2,y2,fill=pen_colour,outline =pen_colour,width= size.get())

canvas.bind('<B1-Motion>',paint)

#***************************************************


win.mainloop()