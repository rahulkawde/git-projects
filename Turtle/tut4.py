import turtle
from turtle import Screen,Turtle

''' mouse dragging '''

screen = Screen()
t= Turtle('turtle')
t.speed(-1)

def dragging(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(dragging)

def clickleft(x,y):
    t.clear()

def main():
    turtle.listen()
    t.ondrag(dragging)
    turtle.onscreenclick(clickleft,1)
    screen.mainloop()


main()            