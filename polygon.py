import turtle

def circle(t, radius):
    # draw a circle using turtle built-in method
    t.circle(radius)

def radialPattern():
    screen = turtle.Screen()
    t = turtle.Turtle()

    t.speed(0)

    for i in range(12):
        circle(t, 100)
        t.left(30)

    turtle.done()
