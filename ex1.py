# Use turtle graphics to make an infinite spiral

from turtle import *

x=1

while True:
    for i in range(2):
        forward(x*10)
        left(90)
    x+=1

exitonclick()
