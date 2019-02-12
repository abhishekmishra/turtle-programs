# pylint: disable=unused-wildcard-import, undefined-variable
from turtle import *

penup()
forward(100)

begin_fill()
circle(-100)
end_fill()

right(90)
forward(80)
left(90)

fillcolor('gray')
begin_fill()
circle(-20)
end_fill()

right(180)
forward(250)
right(90)
forward(80)
right(90)

fillcolor('black')
begin_fill()
circle(-100)
end_fill()

right(90)
forward(80)
left(90)

fillcolor('gray')
begin_fill()
circle(-20)
end_fill()

color('gray', 'black')
forward(105)
pendown()
left(90)
circle(105, 180)

penup()
left(90)
forward(210)

pendown()
forward(43)
left(270)
circle(105, -180)

right(90)
forward(40)
left(90)
forward(150)

left(90)
forward(250)
right(80)
forward(100)

left(80)
forward(150)

left(80)
forward(100)

left(100)
forward(190)

left(180)
forward(100)

right(90)
forward(100 * 0.984)

right(180)
forward(100 * 0.984)

right(90)
forward(200)

left(90)
forward(150)

left(90)
forward(40)

done()
