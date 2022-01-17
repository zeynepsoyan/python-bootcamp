from asyncio.proactor_events import _ProactorDuplexPipeTransport
from turtle import Turtle, Screen
import random

screen = Screen()

height = 400
width = 500
is_race_on = False
screen.setup(height=height, width=width)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > width / 2 - 20:
            winning_color = turtle.pencolor()
            
            if winning_color == user_bet.lower():
                print(f"You've won. The {winning_color} color turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} color turtle is the winner!")

            is_race_on = False

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()