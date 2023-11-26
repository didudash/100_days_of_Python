from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 25, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.color("purple")
        self.penup()
        self._update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self._update_scoreboard()

    def left_point(self):
        self.left_score += 1
        self._update_scoreboard()

    def _update_scoreboard(self) -> None:
        self.clear()
        self.goto(100, 260)
        self.write(
            f"{self.right_score}",
            align=ALIGNMENT,
            font=FONT,
        )
        self.goto(-100, 260)
        self.write(
            f"{self.left_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self) -> None:
        self.color("red")
        self.goto(x=0, y=0)
        self.write(
            f"GAME OVER",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )
