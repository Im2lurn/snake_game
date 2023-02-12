from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-150, 270)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"SCORE : {self.score}   HIGH SCORE : {self.high_score}", font=("courier", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.score_update()

    def increase_score(self):
        self.score += 1
        self.score_update()
