from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self) -> None:
        self.goto(STARTING_POSITION)

    def move_forward(self) -> None:
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(STARTING_POSITION[0], new_y)

    def is_at_finish_line(self) -> bool:
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
