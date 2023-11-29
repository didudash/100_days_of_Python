from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self._read_highest_score()
        self.hideturtle()
        self.color("purple")
        self.penup()
        self.goto(x=0, y=260)
        self._update_scoreboard()

    def _read_highest_score(self):
        with open("data.txt") as file:
            self.highest_score = file.read()
        return int(self.highest_score)

    def _write_highest_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highest_score}")

    def _update_scoreboard(self) -> None:
        self.clear()
        self.write(
            f"Score: {self.score} Highest Score: {self.highest_score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self) -> None:
        self.score += 1
        self._update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self._write_highest_score()
        self.score = 0
        self._update_scoreboard()

    # def game_over(self) -> None:
    #     self.color("red")
    #     self.goto(x=0, y=0)
    #     self.write(
    #         f"GAME OVER",
    #         move=False,
    #         align=ALIGNMENT,
    #         font=FONT,
    #     )
