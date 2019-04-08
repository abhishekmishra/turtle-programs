from picoturtle import *
import math

def chamber(base, s1, s2, a1, a2):
    # save the position of the lower left vertex
    lower_left = state()['location']
    orig_heading = state()['angle']

    # draw the base and right side and save the position of the 
    # upper right vertex (see below)
    forward(base)
    left(a2)
    forward(s2)
    upper_right = state()['location']

    #return to the lower left vertex and draw the left side
    penup()
    setx(lower_left['x'])
    sety(lower_left['y'])
    heading(orig_heading)
    pendown()
    left(a1)
    forward(s1)

    return upper_right

def face(loc):
    s = state()
    m = (loc['y'] - s['location']['y'])/(loc['x'] - s['location']['x'])
    print('-')
    print(math.atan(m))
    required_heading = math.degrees(math.atan(m))
    print(required_heading)
    if required_heading < 0:
        required_heading = 180 + required_heading
    print(required_heading)
    heading(required_heading)

def distance(loc):
    s = state()
    d = math.sqrt(
        math.pow((loc['x'] - s['location']['x']), 2) +
        math.pow((loc['y'] - s['location']['y']), 2)
    )
    return d

def spiral_growth(base, s1, s2, a1, a2):
    # draw one chamber and face along the edge of the new chamber
    upper_right = chamber(base, s1, s2, a1, a2)
    face(upper_right)

    # the length of the next chamber's base is the distance
    # from the current location to the upper right corner of
    # the chamber just drawn
    next_base = distance(upper_right)

    if next_base > 100:
        return

    # compute the ratio of the sides of the new chamber to the 
    # sides of the previous chamber
    r = next_base/base

    # now repeat the process, using as inputs
    # the sides and angles of the new chamber
    spiral_growth(next_base, s1 * r, s2 * r, a1, a2)

if __name__ == "__main__":
    # Create the turtle before using
    create_turtle()

    # Your code goes here #

    heading(0)
    pendown()
    pencolour(255, 0, 0)
    #chamber(10, 10, 15, 90, 90)
    spiral_growth(10, 10, 15, 90, 90)

    # Your code ends here #

    # Always stop the turtle
    stop()
