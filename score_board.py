from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-50, 270)
        self.write(f"SCORE : {self.score}", font=("courier", 15, "normal"))


    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE : {self.score}", font=("courier", 15, "normal"))

    def game_over(self):
        self.goto(-130,0)
        self.write("-GAME OVER-", font=("courier", 30, "bold"))


