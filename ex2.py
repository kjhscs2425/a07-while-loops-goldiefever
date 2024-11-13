# make infinite circles, start with a small circle, then draw a bigger circle around it

from turtle import *

x=1

while True:
    circle((x*10),360)
    up()
    setheading(270)
    forward(10)
    setheading(0)
    down()
    x+=1