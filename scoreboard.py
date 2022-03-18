from turtle import Turtle
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-270, 250)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level:{self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!",align="center", font=FONT)