#TODONE: Create collison with food
#TODONE: Create scoreboard
#TODONE: Detect collision with wall
#TOODNE: Detect collision with tail

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False


    # # Infinite wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280:
    #     new_x = -(snake.head.xcor())
    #     new_y = snake.head.ycor()
    #     snake.head.goto(new_x, new_y)
    # elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     new_x = snake.head.xcor()
    #     new_y = -(snake.head.ycor())
    #     snake.head.goto(new_x,new_y)


    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()