from picoturtle import *


if __name__ == "__main__":
    # Create the turtle before using
    create_turtle()
    
    # Your code goes here #

    def poly(side, angle, incs, inca):
        for i in range(100):
            forward(side)
            right(angle)
            side += incs
            angle += inca

    penup()
    back(50)
    pencolour(255, 0, 0)
    pendown()
    poly(5, 120, 3, 0)
    penup()
    forward(100)
    font('bold 30pt Arial')
    left(30)
    pencolour(0, 255, 0)
    filltext('नमस्ते')
    penup()
    forward(100)
    pendown()
    penwidth(1)
    pencolour(255, 0, 255)
    stroketext('दुनिया')
    penup()
    forward(120)
    home()
    goto(10, 10)
    pendown()
    pencolour(255, 128, 0)
    penwidth(5)
    forward(150)
    setx(40)
    sety(100)
    heading(0)
    s = state()
    print(s)

    # Your code ends here #

    # Always stop the turtle
    stop()
