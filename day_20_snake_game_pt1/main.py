from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_parts = []
part_size = 20
snake_size = 3

for i in range(snake_size):
    new_part = Turtle("square")
    new_part.color("white")
    new_part.penup()
    new_part.goto(x=0 - i * part_size, y=0)
    snake_parts.append(new_part)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for part in range(snake_size - 1, -1, -1):
        print(part)
        new_x = snake_parts[part - 1].xcor()
        new_y = snake_parts[part - 1].ycor()
        print(new_x, new_y)
        snake_parts[part].goto(new_x, new_y)
    snake_parts[0].forward(part_size)
    snake_parts[0].left(90)


screen.exitonclick()
