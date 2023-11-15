from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
tim.shape("turtle")
tim.color("crimson")
# Setting the screen color-mode
screen = Screen()
screen.colormode(255)
tim.speed("fastest")


def turtle_square(length: int) -> None:
    for _ in range(4):
        tim.forward(length)
        tim.right(90)


def turtle_dashed_line(segment_length: int, times_lenghts: int) -> None:
    for _ in range(times_lenghts):
        tim.pendown()
        tim.forward(segment_length)
        tim.penup()
        tim.forward(segment_length)


def random_color() -> tuple:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def turtle_figures(length: int) -> None:
    for sides in range(3, 12):
        angle = 360 / sides
        for _ in range(sides):
            tim.pencolor(random_color())
            tim.forward(length)
            tim.right(angle)


def turtle_random_walk(steps: int, length: int) -> None:
    tim.width(10)
    for _ in range(steps):
        angle = randint(0, 360)
        tim.pencolor(random_color())
        tim.forward(length)
        tim.right(angle)


def turtle_random_walk_4(steps: int, length: int) -> None:
    tim.width(10)
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        tim.pencolor(random_color())
        tim.setheading(choice(directions))
        tim.forward(length)


def turtle_spirograph(size_of_gap: int) -> None:
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


screen.exitonclick()
