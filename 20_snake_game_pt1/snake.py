from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.part_size = 20
        self.snake_size = 3
        self.snake_parts = []
        self._create_snake()
        self.head = self.snake_parts[0]

    def _create_snake(self):
        for i in range(self.snake_size):
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.goto(x=0 - i * self.part_size, y=0)
            self.snake_parts.append(new_part)

    def move(self):
        print(len(self.snake_parts))
        for part in range(self.snake_size - 1, 0, -1):
            new_x = self.snake_parts[part - 1].xcor()
            new_y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(new_x, new_y)
        self.snake_parts[0].forward(self.part_size)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
