from picoturtle import *

def hist(values):
    ymax = 250.0/max(values.values())
    pw = 40
    pencolour(128, 128, 128)
    font('16pt Arial')
    for k, v in values.items():
        pendown()
        penwidth(pw)
        forward(v * ymax)
        filltext(' ' + str(v))
        penup()
        back(v * ymax)
        right(160)
        filltext(' ' + k)
        left(160)
        right(90)
        forward(pw + 2)
        left(90)


if __name__ == "__main__":
    # Create the turtle before using
    create_turtle()

    # Your code goes here #

    back(100)
    right(90)
    back(100)
    left(90)
    hist({
        'apple': 100,
        'orange': 5,
        'mango': 15,
        'pineapple': 25,
        'kiwi': 2
    })

    # Your code ends here #

    # Always stop the turtle
    stop()
