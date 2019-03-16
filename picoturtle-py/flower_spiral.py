from picoturtle import *


if __name__ == "__main__":
    # Create the turtle before using
    create_turtle()

    # Your code goes here #

    pencolour(20, 100, 180)
    penwidth(2)

    for angle in range(0, 190, 10):
        penup()
        home()
        heading(angle)
        pendown()

        for i in range(180):
            left(1)
            back(1)

        penup()
        home()
        heading(angle)
        pendown()

        for i in range(180):
            left(1)
            forward(1)

        # clear()

    # Your code ends here #

    # Always stop the turtle
    stop()
