from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, food_radius: int):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=food_radius / 20, stretch_len=food_radius / 20)
        self.color("green")
        self.speed("slowest")
        self.refresh()

    def refresh(self) -> None:
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
