from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 60, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player2_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.player1_score, align=ALIGNMENT, font=FONT)


    def player1_scores(self):
        self.player1_score += 1
        self.update_scoreboard()

    def player2_scores(self):
        self.player2_score += 1
        self.update_scoreboard()