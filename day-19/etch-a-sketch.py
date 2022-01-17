from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()

def move_forwards():
    jim.forward(10)

def move_backwards():
    jim.backward(10)

def rotate_clockwise():
    jim.right(10)

def rotate_counterclockwise():
    jim.left(10)

def clear():
    jim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()