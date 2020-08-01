# YOUTUBE DOWNLOADER√√√
import youtube_dl
import tkinter as tk

win = tk.Tk()
win.title('YouTube Downloader')
win.geometry('300x200')

opts = {'outtmpl':'./videos/%(title)s.%(ext)s',}

def ytdl(x):
    with youtube_dl.YoutubeDL(opts) as y:
        t = y.download([x])

def ytl():
    v= entry.get()
    entry.delete(0,'end')
    if len(v) !=0:
        ytdl(v)
    else:
        print('Not Done')    


photo = tk.PhotoImage(file = 'practice/projects/YT Downloader/img.png')
label = tk.Label(win,image=photo)
label.pack()
label1 = tk.Label(win,text= 'Enter your link:')
label1.pack()
entry = tk.Entry(win,width = 20)
entry.pack()
button = tk.Button(win,text='Download',command=ytl)
button.pack()
win.mainloop()