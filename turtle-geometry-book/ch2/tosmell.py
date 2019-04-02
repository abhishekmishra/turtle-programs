from picoturtle import *
import math
import random

prev_dist = -1

def distance(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

def stink(min_d, max_d):
    random.seed()
    x = random.uniform(min_d, max_d)
    y = random.uniform(min_d, max_d)
    stink_loc = {
        'x': x,
        'y': y
    }
    s = state()
    sx = x - 3
    sy = y - 3
    # goto(sx, sy)
    setx(sx)
    sety(sy)
    pendown()
    pencolour(255, 0, 128)
    for i in range(360):
        right(1)
        forward(.1)

    penup()
    setx(s['location']['x'])
    sety(s['location']['y'])
    return stink_loc


def smell(new_dist):
    global prev_dist
    if prev_dist == -1 or new_dist <= prev_dist:
        res = 'stronger'
    else:
        res = 'weaker'
    prev_dist = new_dist
    return res

def find_by_smell(stink_loc, turn):
    global prev_dist
    while prev_dist == -1 or prev_dist > 5:
        forward(1)
        current_loc = state()['location']
        d = distance(current_loc['x'], current_loc['y'],
            stink_loc['x'], stink_loc['y'])
        if smell(d) == 'weaker':
            right(turn)


if __name__ == "__main__":
    # Create the turtle before using
    create_turtle()

    # Your code goes here #

    stink_loc = stink(300, 400)
    pendown()
    pencolour(0, 255, 0)
    find_by_smell(stink_loc, 45)

    # Your code ends here #

    # Always stop the turtle
    stop()
