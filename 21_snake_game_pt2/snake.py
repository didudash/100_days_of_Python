from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.part_size = 20
        self.snake_size = 3
        self.snake_parts = []
        self._create_snake()
        self.head = self.snake_parts[0]

    def _create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            self._add_snake_part(position)

    def _add_snake_part(self, position: tuple) -> None:
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.snake_parts.append(new_part)

    def extend(self) -> None:
        self._add_snake_part(self.snake_parts[-1].position())

    def move(self) -> None:
        for part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part - 1].xcor()
            new_y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(new_x, new_y)
        self.snake_parts[0].forward(self.part_size)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self) -> None:
        # clearing old snake
        for snake_part in self.snake_parts:
            # going to a part that is not in the screen
            snake_part.goto(1000, 100)
        self.snake_parts.clear()
        self._create_snake()
        self.head = self.snake_parts[0]
