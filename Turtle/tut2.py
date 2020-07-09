import turtle
import random
''' in this tut we just change colour and using random module we create random circle'''

tom = turtle.Turtle()
tom.pensize(10)

colours = ['red','blue','black','yellow','green']

tom.color('red','blue')
# for circle
tom.begin_fill()
tom.circle(60)
tom.end_fill()

tom.penup()
tom.forward(200)
tom.pendown()

#color for square
tom.color('yellow','black')
# for square:
tom.begin_fill()
for i in range(4):
    tom.forward(100)
    tom.left(90)
tom.end_fill()

#************************* for random circle: ************************

for i in range(10):
    # circle colours:
    randcolor = random.randrange(0,len(colours)) 
    tom.color(colours[randcolor],colours[random.randrange(0,len(colours))])
    # for positions of circles:
    rand1 = random.randrange(-300,300)
    rand2 = random.randrange(-300,300)
    # for invisible;
    tom.penup()
    tom.setpos(rand1,rand2)
    tom.pendown()

    # create circle:
    tom.begin_fill()
    tom.circle(random.randrange(0,90))
    tom.end_fill()