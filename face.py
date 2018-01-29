from turtle import *

# move to right eye
color('white', 'black')
left(45)
fd(100)

# make an eye
right(45)
color('red', 'black')
fillcolor('red')
begin_fill()
circle(20)
end_fill()

fillcolor('black')
begin_fill()
circle(8)
end_fill()

# move back
color('white', 'black')
home()

# move to right eye
left(135)
fd(100)

# make the right eye
left(45)
color('red', 'black')
fillcolor('red')
begin_fill()
circle(-20)
end_fill()

fillcolor('black')
begin_fill()
circle(-8)
end_fill()

# move back
color('white', 'black')
home()

# make nose
left(90)
color('black', 'black')
fd(50)

left(180)
fd(50)

left(90)
fd(10)

left(180)
fd(20)

# move back
home()
color('white', 'black')

# move to mouth
right(90)
fd(50)
color('red', 'black')
left(90)
circle(50, 45)

# move back
color('white', 'black')
home()

# move to mouth
right(90)
fd(50)
color('red', 'black')
right(90)
circle(-50, 45)

# move back
color('white', 'black')
home()

# make face
color('black', 'black')
fd(10)
color('white', 'black')
fd(140)
left(90)
color('red', 'black')
circle(150)

# make left ear
right(90)
circle(25, 200)

right(90)
color('red', 'black')
circle(150, 30)

pensize(15)
color('black', 'black')
circle(150, 80)

pensize(0)
color('red', 'black')
circle(150, 30)

right(90)
circle(25, 200)
