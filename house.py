from turtle import *

def rectangle(h, w):
    pendown()
    forward(w)
    left(90)
    forward(h)
    left(90)
    forward(w)
    left(90)
    forward(h)

penup()
right(90)
forward(200)
right(90)
forward(200)
right(180)

color('black', 'black')
rectangle(300, 400)
