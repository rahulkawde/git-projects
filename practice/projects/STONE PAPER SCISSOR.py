# Stone Paper Scissor Game
import random
from tkinter import *


stats = []

def winner(call):
    if random.random() <= (1/3):
        throw = 'scissors'
    elif (1/3) < random.random() <= (2/3) :
        throw  = 'rock'
    else:
        throw = 'paper'

    if (throw  == 'rock' and call== 'scissors')  or (throw  == 'scissors' and call== 'paper') or (throw  == 'paper' and call== 'rock'):
        stats.append('W')
        result = 'You Won'
    elif throw==call :
        stats.append('D')  
        result= 'Match Draw'   
    else:
        stats.append('L')
        result = 'You Lost'  

    global output
    output.config(text='Computer did:' + throw + '\n' + result)   # see com o/p

def press_s():
    winner('scissors')    
def press_r():
    winner('rock') 
def press_p():
    winner('paper')         


win = Tk()
win.title('Stone Paper Scissor Game')

stone=  Button(win,text='Stone',font='helvetica 20 bold',padx=5,pady=5,command=press_r,width=26)
paper=  Button(win,text='Paper',font='helvetica 20 bold',padx=5,pady=5,command=press_p,width=26)
scissors= Button(win,text='Scissors',font='helvetica 20 bold',padx=5,pady=5,command=press_s,width=26)
output= Label(win,text = ' What\'s Your Call ?',font='helvetica 19 bold')

stone.pack(side=LEFT)
paper.pack(side=LEFT)
scissors.pack(side=LEFT)
output.pack(side=RIGHT)

win.mainloop()
# result show
for i in stats:print(i,end='')
if stats.count('L') > stats.count('W'):
    result = '\nYou Loose Match'
elif stats.count('L') == stats.count('W'):
    result = '\nDraw Match'
else:
    result = '\nYou Win Match'

print(result)