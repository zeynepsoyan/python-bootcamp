from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()

def move_forward():
    jim.forward(10)


jim.listen()
jim.onkey()