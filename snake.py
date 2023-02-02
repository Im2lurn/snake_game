from turtle import Turtle

move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    snake_body = []

    def __init__(self, ):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for _ in range(3):
            position = (0 - (_ * 20), 0)
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_piece = Turtle(shape="square")
        new_snake_piece.color("purple")
        new_snake_piece.penup()
        self.snake_body.append(new_snake_piece)
        new_snake_piece.goto(position)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())
