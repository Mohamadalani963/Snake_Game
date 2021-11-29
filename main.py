from turtle import Screen,Turtle
import time
from food import Food
from scoreBoard import Scoreboard
from snake import Snake

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreBoard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

game_is_on = True

while game_is_on:

    screen.update()
    snake.move()
    if scoreBoard.score == 0:
        time.sleep(0.1-(scoreBoard.score/10))
    else:
        time.sleep(0.1)

    # detect interacting with food
    if snake.head.distance(food)<20:
        food.refresh()
        scoreBoard.increaseScore()
        snake.extends()

    # detect touching the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        game_is_on = False
        scoreBoard.gameOver()

    # detect touching the tail
    for segment in snake.segment[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreBoard.gameOver()









screen.exitonclick()
