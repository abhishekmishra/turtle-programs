from picoturtle import *
create_turtle()

### Your code goes here ###

def tree(size):
    if size < 16:
        forward(size)
        forward(-size)
        return
    
    forward(size/4)

    left(40)
    tree(size/2)
    right(40)

    forward(size/4)

    right(35)
    tree(size/2)
    left(35)

    forward(size/4)

    left(30)
    tree(size/2)
    right(30)

    forward(size/4)

    right(25)
    tree(size/2)
    left(25)

    forward(-size)

forward(-200)
pendown()
pencolour(0, 128, 0)
tree(128)

### Your code ends here ###

### Always stop the turtle
stop()