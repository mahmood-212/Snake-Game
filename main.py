from turtle import Screen, Turtle
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import random
import time

random_x = random.randint(-280, 280)
random_y = random.randint(-280, 280)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Original Snake Game")
screen.tracer(0)
snakey = Snake()
score_board = Scoreboard()

screen.listen()
food_point = Food()
screen.onkey(fun=snakey.up, key="Up")
screen.onkey(fun=snakey.down, key="Down")
screen.onkey(fun=snakey.left, key="Left")
screen.onkey(fun=snakey.right, key="Right")

is_game_on = True
while is_game_on:
    # score_board.score
    screen.update()
    time.sleep(0.1)
    snakey.move()
    score_board.score

    if snakey.head.distance(food_point) < 15:
        food_point.move_food()
        score_board.score += 1
        score_board.clear()
        snakey.n1 += 1
        snakey.extend()
        score_board.write(f"Score: {score_board.score}", align="center", font=("Arial", 22, "normal"))

    # Detect collision with wall.
    if snakey.head.xcor() < -280 or snakey.head.xcor() > 280 or snakey.head.ycor() > 280 or snakey.head.ycor() < -280:
        is_game_on = False
        score_board.goto(0, 0)
        score_board.game_over()

    # Detect collision with snake tail
    for snake2 in snakey.snake_list[1::]:
        # if head collision with ant segment in the tail
        if snakey.head.distance(snake2) < 10:
            # trigger game_over
            is_game_on = False
            score_board.goto(0, 0)
            score_board.game_over()


screen.exitonclick()