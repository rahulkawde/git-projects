import tkinter as tk
from tkinter import font
from tkinter import ttk
from pytube import YouTube


win = tk.Tk()
win.title('YouTube Downloader')
win.iconbitmap('practice/projects/YT Downlaoder/download.ico')
win.geometry('300x200')

def download():
    search = entry_var.get()
    # print(search)
    yt = YouTube(search)
    videos = yt.streams.all()
    # print(videos)
    i = 1
    for stream in videos:
        optn = ((str(i)+' '+ str(stream)))
        i+=1
    print(stream)
    
    # stream_no = option_var.get()
    # stream_no = pass
    video = videos[stream -1]
    video.download('/Users/sachinkawde/Downloads')  

    tk.Label(win,text= 'Download Complete',font='helvetica 12').grid(row=7,column=3)

    
photo = tk.PhotoImage(file = 'practice/projects/YT Downloader/img.png')
label = tk.Label(win,image=photo)
label.grid(row=0,column=3)

link = tk.Label(win,text = 'Link',font='helvetica 12 bold')
link.grid(row=3,column= 0)

entry_var = tk.StringVar()
entry = tk.Entry(win, width = 30,textvariable= entry_var)
entry.grid(row=3,column=3)

option_var = tk.StringVar()
option = ttk.Combobox(win,width = 10,textvariable= option_var ,state = 'readonly')
option['values'] = ('1080','720','480','360')
option.grid(row=4,column=3)

button = tk.Button(win,text = 'Download',font='helvetica 12 bold',command=download)
button.grid(row = 6, column = 3)

win.mainloop()