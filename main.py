from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

# creating objects
snake = Snake()
food = Food()
score = Score()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_update()
        snake.extend()

    # detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # detect collision with tail
    # using slicing
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
