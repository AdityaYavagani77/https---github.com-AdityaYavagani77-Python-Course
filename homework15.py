
#Do NOt Run both at same time

#For the House

import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(0)

side_length = 80

for i in range(4):
    t.forward(side_length)
    t.left(90)

t.left(90)
t.forward(side_length)
t.right(90)

t.left(60)
t.forward(side_length)
t.right(120)
t.forward(side_length)
t.right(120)
t.forward(side_length)

turtle.done()

#For the Spiral

import turtle

t = turtle.Turtle()
t.speed(0)

segment_length = 5
turn_angle = 15

for i in range(100):
    t.forward(segment_length)
    t.right(turn_angle)
    segment_length = segment_length + 2

turtle.done()
