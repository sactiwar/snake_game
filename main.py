from turtle import Turtle,Screen
from snake import Snake
from food import Food
from colliosion import Colliosion
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=700,height=700)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
food = Food()
boundary = Colliosion()
score_num = Score()
is_race_on = True
while is_race_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    snake.listen()

    if snake.snake_list[0].distance(food) < 15:
        food.new_food()
        score_num.increase_score()
        snake.extend()

    if snake.snake_list[0].xcor() >340 or snake.snake_list[0].xcor()< -340:
        score_num.game_over()
        is_race_on = False
    elif snake.snake_list[0].ycor() >340 or snake.snake_list[0].ycor()< -340:
        score_num.game_over()
        is_race_on = False

    for i in snake.snake_list:
        if i==snake.snake_list[0]:
            pass
        elif snake.snake_list[0].distance(i)<10:
           score_num.game_over()
           is_race_on = False


screen.exitonclick()