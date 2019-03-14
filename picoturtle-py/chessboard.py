from picoturtle import *
create_turtle()

### Your code goes here ###

def dark_square(side):
    penwidth(side)
    forward(side)

def square(side):
    penwidth(1)
    for i in range(4):
        forward(side)
        right(90)

penup()
left(90)
forward(100)
right(90)
forward(-200)

pendown()
pencolour(165, 42, 42)
for i in range(4):
    for i in range(4):
        pendown()
        dark_square(30)
        penup()
        left(90)
        forward(15)
        right(90)
        pendown()
        square(30)
        penup()
        right(90)
        forward(15)
        left(90)
        forward(30)
        penup()
    forward(-240)
    right(90)
    forward(30)
    left(90)
    for i in range(4):
        left(90)
        forward(15)
        right(90)
        pendown()
        square(30)
        penup()
        right(90)
        forward(15)
        left(90)
        forward(30)
        penup()
        pendown()
        dark_square(30)        
        penup()
    forward(-240)
    right(90)
    forward(30)
    left(90)

### Your code ends here ###

# Always stop the turtle
stop()