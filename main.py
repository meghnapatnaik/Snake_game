from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
level = screen.textinput(title="Level", prompt="Choose the level: Easy, Medium,Hard")
level = level.lower()
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()

    if level == "easy":
        time.sleep(0.3)
        snake.move()
    elif level == "medium":
        time.sleep(0.2)
        snake.move()
    elif level == "hard":
        time.sleep(0.1)
        snake.move()

    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        score.increment_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
