from picoturtle import Turtle

def polyspi(t, dist, angle, incd, inca):
    for i in range(25):
        t.forward(dist)
        t.right(angle)
        dist += incd
        angle += inca

t = Turtle()
t.turtle_init()
t.pendown()
t.pencolour(0, 0, 255)
polyspi(t, 20, 145, 5, 0)
t.stop()
