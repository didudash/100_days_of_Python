from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("purple")
        self.penup()
        self.goto(x=0, y=260)
        self._update_scoreboard()

    def _update_scoreboard(self) -> None:
        self.write(
            f"Score: {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self._update_scoreboard()

    def game_over(self) -> None:
        self.color("red")
        self.goto(x=0, y=0)
        self.write(
            f"GAME OVER",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )
