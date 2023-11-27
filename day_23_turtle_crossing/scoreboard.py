from turtle import Turtle

FONT = ("Comic Sans MS", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(
            f"Level: {self.level}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self) -> None:
        self.color("red")
        self.goto(x=0, y=0)
        self.write(
            f"GAME OVER :(",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )
