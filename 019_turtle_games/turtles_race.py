from turtle import Turtle, Screen
import random
from typing import List


def equidistant_turtles(
    lower_bound: int, higher_bound: int, num_turtles: int
) -> List[float]:
    """Calculate equidistant points for turtle positions."""
    distance = (higher_bound - lower_bound) / (num_turtles - 1)
    points = [lower_bound + i * distance for i in range(num_turtles)]
    return points


colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def turtles_race(
    screen_width: int,
    screen_height: int,
    lower_bound: int,
    higher_bound: int,
    num_turtles: int,
) -> None:
    """Function to run the turtle race."""
    screen = Screen()
    screen.setup(width=screen_width, height=screen_height)

    # Normalize user input to lowercase
    user_bet = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
    )
    if user_bet:
        user_bet = user_bet.lower()

    # Object state and instances
    x_pos = -screen_width / 2 + 20
    y_pos = equidistant_turtles(lower_bound, higher_bound, num_turtles)
    all_turtles: List[Turtle] = []

    for i in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=x_pos, y=y_pos[i])
        all_turtles.append(new_turtle)

    is_race_on = bool(user_bet)

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > (screen_width - 40) / 2:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost :( The {winning_color} turtle is the winner!")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    screen.exitonclick()


# Parameters
screen_width = 500
screen_height = 400
lower_bound = -80
higher_bound = 80
num_turtles = 6

turtles_race(screen_width, screen_height, lower_bound, higher_bound, num_turtles)
