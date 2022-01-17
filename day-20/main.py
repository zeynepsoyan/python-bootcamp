#TODONE: Create a snake body
#TODONE: Move the snake
#TODONE: Control the snake

#TODONE: Create collison with food
#TODONE: Create scoreboard
#TODONE: Detect collision with walls
#TOODNE: Detect collision with tail

from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()