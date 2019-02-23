from picoturtle import *
create_turtle()

### Your code goes here ###

def spiral(distance, angle, pwidth, distance_inc, angle_inc, pwidth_inc):
    x = distance
    a = angle
    pw = pwidth
    for i in range(100):
        penwidth(pw)
        forward(x)
        right(a)
        x += distance_inc
        a += angle_inc
        pw += pwidth_inc

pencolour(255, 128, 0)
pendown()
spiral(1, 30, 1, 1, 0, 0.1)

### Your code ends here ###

# Always stop the turtle
stop()