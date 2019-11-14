import turtle
bob = turtle.Turtle()

def polygon(distance,sides,color):
    bob.color(color)
    angle = 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance,color):
    bob.color(color)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.right(144)
    bob.end_fill()

def explosion(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
    bob.end.fill()

def starship():
    for times in range(100):
        c=(times*2,0,times*2)
        star

