"""
import turtle

User = int(input("Please enter a the number of sides you want on you shape:"))

t = turtle.Turtle()
t.color("blue")
t.fillcolor("orange")

t.begin_fill()

t.pensize(3)

for i in range(User):
    t.forward(100)
    t.right(360/User)

t.end_fill()

turtle.done()
"""

import turtle

t = turtle.Turtle()

t.color("blue")
t.fillcolor("pink")

t.pensize(7)

t.up()

t.goto(89,76)

t.down()

t.begin_fill()

t.circle(77)

t.end_fill()

t.color("orange")
t.fillcolor("red")

t.up()

t.goto(1,298)

t.down()

t.begin_fill()

t.circle(89)

t.end_fill()

t.color("brown")
t.fillcolor("purple")

t.up()

t.goto(-42,8)

t.down()

t.begin_fill()

t.circle(69)

t.end_fill()

