from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

FOOD_RADIUS = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food(FOOD_RADIUS)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # Detecting collission with food
    # And extending the snake
    # Plus for overhead
    if snake.head.distance(food) < FOOD_RADIUS + 5:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detecting collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()
        # game_is_on = False
        # scoreboard.game_over()

    # Detecting collision with tail
    for snake_part in snake.snake_parts[1:]:
        if snake.head.distance(snake_part) < 10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over()


screen.exitonclick()
