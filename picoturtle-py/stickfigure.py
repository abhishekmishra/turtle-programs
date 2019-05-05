from picoturtle import *
import math

def stick_figure(height, width):
    pendown()

    # make the torso (single line)
    torso_len = height * 0.3   
    forward(torso_len)
    
    # make the head
    head_dia = height * 0.2
    head_circumference = math.pi * head_dia
    right(90)
    for i in range(360):
        left(1)
        forward(head_circumference/360)

    right(90)
    penup()
    forward(torso_len)
    pendown()

    # make the legs
    legs_angle = 60
    leg_height = height * 0.5
    leg_len = math.sin(math.radians(legs_angle/2)) * leg_height
    right(legs_angle/2)
    forward(leg_len)
    back(leg_len)

    left(legs_angle)
    forward(leg_len)
    back(leg_len)

    right(legs_angle/2)
    penup()
    right(180)

    # make the arms
    pendown()
    arms_len = width
    forward(torso_len/2)
    right(90)
    forward(arms_len/2)
    back(arms_len/2)
    left(180)
    forward(arms_len/2)
    back(arms_len/2)
    right(90)

    back(torso_len/2)

    penup()


if __name__ == "__main__":
    # Create the turtle before using
    create_turtle()

    # Your code goes here #

    pencolour(0, 255, 0)
    penup()
    forward(210)
    for i in range(1, 360, 10):
        stick_figure(50, 25)
        right(90)
        forward(35)
        left(80)

    pencolour(200, 100, 0)
    penwidth(5)
    setx(265)
    sety(250)

    stick_figure(100, 50)
    # Your code ends here #

    # Always stop the turtle
    stop()
