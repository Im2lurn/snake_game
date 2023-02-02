from turtle import Turtle
import random


# making Turtle class super of Food class
class Food(Turtle):

    def __init__(self):
        # inheriting from Turtle class
        super().__init__()
        self.shape("circle")
        self.penup()
        # making food size half of default
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    # making food move from pace to place
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
