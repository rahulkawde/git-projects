import turtle
import random
''' we using left right up down click  to create path and change color and stamp'''

tom = turtle.Turtle()
tom.width(5)
tom.speed(0)

colours = ['red','yellow','blue','black','green']

def up ():
    tom.setheading(90)
    tom.forward(100)

def down ():
    tom.setheading(270)
    tom.forward(100)
  
def left ():
    tom.setheading(180)
    tom.forward(100)
  
def right ():
    tom.setheading(0)
    tom.forward(100)
  
def clickleft(x,y):
    tom.color(random.choice(colours))

def clickright(x,y):
    tom.stamp()    


turtle.listen()

turtle.onscreenclick(clickleft,1)
turtle.onscreenclick(clickright,3)

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')  
turtle.onkey(left, 'Left')  
turtle.onkey(right, 'Right')

turtle.mainloop()

            

