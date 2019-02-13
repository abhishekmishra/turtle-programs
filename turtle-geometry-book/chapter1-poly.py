# pylint: disable=unused-wildcard-import, undefined-variable
from turtle import *

# none of the procedures in this file terminate
# implemented as defined in Chapter#1 first part.
# terminating versions will be defined later.

def poly(side, angle):
    forward(side)
    right(angle)
    poly(side, angle)

# poly(100, 125)

def polyspi(side, angle, inc):
    forward(side)
    right(angle)
    polyspi(side+inc, angle, inc)

polyspi(10, 35, 5)
