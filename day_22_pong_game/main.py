from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
# Turning off the animation
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

game_is_on = True
while game_is_on:
    # Turning on the animation
    screen.update()
    screen.listen()
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "x")
    screen.onkey(left_paddle.down, "y")


# create ball and make it move

# detect collision with wall and bounce

# detect collision with paddle

# detect when paddle misses

# keep score

screen.exitonclick()