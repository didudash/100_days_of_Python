from turtle import Turtle


PADDLE_LENGHT = 100


class Paddle:
    def __init__(self, x_pos):
        self.x_pos = x_pos
        self.y_pos = 0
        self.width = 20
        self.height = 100
        self.paddle_lenght_parts = PADDLE_LENGHT / 20
        self.paddle_parts = []
        self._create_paddle()

    def _create_paddle(self):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(self.x_pos, self.y_pos)

    def up(self) -> None:
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self) -> None:
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
