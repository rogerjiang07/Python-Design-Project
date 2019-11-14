#program file
from JiangFunction import*

bob.speed(0)
turtle.bgcolor("black")
turtle.colormode(255)

x = 1

while x < 400:
    for c in["white","green","red"]:
        bob.color(c)
        bob.forward(50 + x)
        bob.right(90.911)
        x=x+1


