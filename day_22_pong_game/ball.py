from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("green")
        self.goto(position)
        # lower number makes it easier to play
        self.x_move = 7
        self.y_move = 7
        self.move_speed = 0.1

    def move(self) -> None:
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        # Reversing direction
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        # Reversing direction
        self.y_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
