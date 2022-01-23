# TODONE: Create the screen
# TODONE: Create and move a paddle
# TODONE: Create another paddle
# TODONE: Create the ball and make it move
# TODONE: Detect collision with wall and bounce
# TODONE: Detect collision with paddle
# TODONE: Detect when paddle misses
# TODONE: Keep score

from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong Game")

scoreboard = Scoreboard()
player1 = Paddle((350,0))
player2 = Paddle((-350,0))
ball = Ball()

screen.listen()

screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")
 
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    # Detect when player1 misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player2_scores()
    
    # Detect when player2 misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.player1_scores()

screen.exitonclick()