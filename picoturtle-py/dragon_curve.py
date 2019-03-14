from picoturtle import *
create_turtle()

### Your code goes here ###

def dragonCurve(order, length):
  right(order * 45)
  dragonCurveRecursive(order, length, 1)

def dragonCurveRecursive(order, length, sign):
  if order == 0:
    forward(length)
  else:
    rootHalf = (1 / 2) ** (1 / 2)
    dragonCurveRecursive(order - 1, length * rootHalf, 1)
    right(sign * -90)
    dragonCurveRecursive(order - 1, length * rootHalf, -1)

penup()
pencolour(255, 0, 0)
penwidth(1.5)
back(150)
pendown()
dragonCurve(11, 300)

### Your code ends here ###

### Always stop the turtle
stop()