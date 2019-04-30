from picoturtle import *
from pathlib import Path
from os import path


if __name__ == "__main__":
    # Create the turtle before using
    create_turtle()

    # Your code goes here #

    canvas_size(250, 250)
    s = state()
    goto(s['canvas_size']['width']/2, s['canvas_size']['height']/2)

    pencolour(20, 100, 180)
    penwidth(2)

    for angle in range(0, 190, 10):
        penup()
        goto(s['canvas_size']['width']/2, s['canvas_size']['height']/2)
        heading(angle)
        pendown()

        for i in range(180):
            left(1)
            back(1)

        penup()
        goto(s['canvas_size']['width']/2, s['canvas_size']['height']/2)
        heading(angle)
        pendown()

        for i in range(180):
            left(1)
            forward(1)

    export_img(path.join(str(Path.home()), 'turtle-export', 'turtle-' + s['name'] + '.png'))

    # Your code ends here #

    # Always stop the turtle
    stop()
