import turtle
import configparser

def setup_turtle(config):

    t = turtle.Turtle()

    color = config.get("turtle", "pencolor")

    t.pencolor(color)

    return t


config = configparser.ConfigParser()
config.read("turtle_config.ini")

t = setup_turtle(config)

for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()
