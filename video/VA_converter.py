# import tkinter as tk
# from tkinter import filedialog
# import ffmpeg 
# # import moviepy.editor as mp

# win = tk.Tk()
# win.title('Video Audio Converter')


# # def browsefunc():
# #     filename =tk.filedialog.askopenfilename(filetypes=(("mp4 files"," *.mp4"),("All files","*.*")))
# #     v_ent.insert(tk.END, filename)



# def convert():
#     # v_path = video_var.get()
#     # # a_path = audio_var.get()

#     # print(v_path)
#     # # print(a_path)
#     # clip = mp.VideoFileClip(r'v_path')
#     # clip.audio.write_audiofile(r'prctice/v.mp3')

    

    


# photo = tk.PhotoImage(file ='video/video.png' )
# tk.Label(win,image = photo).grid(row=0,column=2)
# video_var=tk.StringVar()
# v_ent =tk.Entry(win,width=25,textvariable= video_var)
# v_ent.grid(row=1,column=2)
# b1=tk.Button(win,text="browse",command=browsefunc)
# b1.grid(row=1,column=4)


# photo2 = tk.PhotoImage(file ='video/audio.png')
# tk.Label(win,image = photo2).grid(row=2,column=2)
# # audio_var=tk.StringVar()
# # tk.Entry(win,width=25).grid(row=3,column=2)
# # b1=tk.Button(win,text="DEM",command=browsefunc)
# # b1.grid(row=3,column=4)

# tk.Button(win,text= 'Convert',command = convert).grid(row=3,column=2)


# win.mainloop()


import tkinter as tk
import os
import glob
import subprocess, sys

win = tk.Tk()

label1 = tk.Label(win,text = 'choose video:')
label1.pack()

lst = tk.Listbox(win)
lst.pack()

def convert():
    string = f'ffmprg -i {entry.get()} -f mp3 -ab 192000 -vn audio.mp3'
    # os.system(string)
    # os.startfile('audio.mp3')
    opener = sting if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, 'audio.mp3']


def add_to_entry(event):
    n = lst.curselection()
    item =lst.get(n)
    v.set(item)


for i in glob.glob('*.mp4'):
    lst.insert(tk.END,i)
lst.bind('<Double-Button>',add_to_entry)    

v = tk.StringVar()
entry = tk.Entry(win,textvariable = v)
entry.pack()

button = tk.Button(win,text ='convert',command = convert)
button.pack()
win.mainloop()