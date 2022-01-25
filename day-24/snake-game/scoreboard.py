from importlib.resources import contents
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0
        self.high_score = self.read_data()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.write_data()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_data(self):
        with open("data.txt", mode="r") as data:
            return int(data.read())

    def write_data(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))