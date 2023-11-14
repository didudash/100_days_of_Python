from turtle import Turtle, Screen
from random import randint, choice
import colorgram

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.color("white")
tim.speed("fastest")


rgb_colors = []
# inspiration painting for the color palette
colors = colorgram.extract("painting.jpg", 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))


def teleport(turtle_obj, x, y) -> None:
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()


def hirst_painting(radius, space, x_start=-270, y_start=-270) -> None:
    for line in range(10):
        teleport(tim, x_start, y_start + (space) * (line))
        for _ in range(10):
            tim.dot(radius, choice(rgb_colors))
            tim.penup()
            tim.forward(space)


hirst_painting(20, 50)


screen.exitonclick()
