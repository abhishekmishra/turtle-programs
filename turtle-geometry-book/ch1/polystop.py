from picoturtle import *

def polystop(side, angle):
    turn = 0
    while True:
        forward(side)
        right(angle)
        turn = turn + angle
        if turn % 360 == 0:
            break

if __name__ == "__main__":
    # Create the turtle before using
    create_turtle()

    # Your code goes here #

    pencolour(255, 128, 0)
    pendown()
    polystop(50, 30)

    # Your code ends here #

    # Always stop the turtle
    stop()
