import turtle
import math

pi = math.pi
print(pi)
bob = turtle.Turtle()

def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon_arc(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r , angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def circle(t,r):
    arc(t, r, 360)

 

circle(bob, 70)
turtle.mainloop()

    
