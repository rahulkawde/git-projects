#Digital clock√√√
import tkinter as tk
import time
# define clock
def clock_time():
    current_time = time.strftime('%I:%M:%S:%P')
    label = tk.Label(win,text= current_time,font = 'berlin 80 bold',bg ='white',fg='black')
    label.after(200,clock_time)
    label.grid(row = 0, column = 0)


win = tk.Tk()
win.title('Digital Clock')
win.resizable(0,0)
clock_time()
win.mainloop()

