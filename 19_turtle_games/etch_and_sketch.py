from turtle import Turtle, Screen
from typing import Callable, Dict

tim = Turtle()
screen = Screen()

STEP_SIZE = 50
ANGLE = 30


def move_forwards() -> None:
    tim.forward(STEP_SIZE)


def move_backwards() -> None:
    tim.backward(STEP_SIZE)


def move_counter_clockwise() -> None:
    tim.circle(radius=STEP_SIZE, extent=ANGLE)


def move_clockwise() -> None:
    tim.circle(radius=STEP_SIZE, extent=-ANGLE)


def clear_screen() -> None:
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def etch_and_sketch() -> None:
    # Key mappings
    key_actions: Dict[str, Callable[[], None]] = {
        "w": move_forwards,
        "s": move_backwards,
        "a": move_counter_clockwise,
        "d": move_clockwise,
        "c": clear_screen,
    }
    # Event Listeners
    screen.listen()
    for key, action in key_actions.items():
        screen.onkey(fun=action, key=key)  # Lowercase
        screen.onkey(fun=action, key=key.upper())  # Uppercase
    screen.exitonclick()


etch_and_sketch()
