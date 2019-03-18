from picoturtle import *
from polystop import *
import time

def polyroll(side, angle1, angle2):
    for i in range(20):
        polystop(side, angle1)
        right(angle2)
        state()
        time.sleep(0.5)


if __name__ == "__main__":
    # Create the turtle before using
    create_turtle()

    # Your code goes here #

    penwidth(5)
    pencolour(128, 128, 0)
    polyroll(100, 60, 20)

    #polyroll(100, 60, 45)

    # Your code ends here #

    # Always stop the turtle
    stop()
