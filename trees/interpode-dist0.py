from picoturtle import *
create_turtle()

### Your code goes here ###

def tree(size, interpode_fn):
    if size < 4:
        forward(size)
        forward(-size)
        return
    
    start_state = state()
    forward(interpode_fn(size, 0))

    left(60)
    tree(interpode_fn(size, 1), interpode_fn)
    right(60)

    forward(interpode_fn(size, 1))

    right(35)
    tree(size/2, interpode_fn)
    left(35)

    forward(interpode_fn(size, 2))

    left(30)
    tree(size/2, interpode_fn)
    right(30)

    forward(interpode_fn(size, 3))

    right(25)
    tree(size/2, interpode_fn)
    left(25)

    #forward(-size)
    goto(start_state['location']['x'], start_state['location']['y'])

penup()
back(100)
pendown()
pencolour(165, 42, 42)
s = state()
print(s)
tree(16, lambda size, num: size/(num + 1))

### Your code ends here ###

### Always stop the turtle
stop()