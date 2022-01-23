import turtle as t
# from turtle import *
# import turtle as t -> t.Turtle()

jim = t.Turtle()
jim.shape("turtle")
jim.color("aquamarine3")

# Challange 1 - Draw a square
for _ in range(4):
    jim.forward(100)
    jim.right(90)

# Challange 2 - Draw a dashed line
for _ in range(15):
    jim.forward(10)
    jim.penup()
    jim.forward(10)
    jim.pendown()

# Challange 3 - Draw different shapes
import random
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "salmon", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        jim.forward(100)
        jim.right(angle)

for side_n in range(3,11):
    jim.color(random.choice(colors))
    draw_shape(side_n)

# Challange 4 - Random walk
import random
colors = ["pale turquoise", "medium turquoise", "steel blue", "light green", "pale goldenrod", "salmon", "pale violet red", "orange"]
directions = [0, 90, 180, 270]

jim.pensize(5)
jim.speed("fast")

for _ in range(200):
    jim.color(random.choice(colors))
    jim.setheading(random.choice(directions))
    jim.forward(30)
    pass

# Challange 4.2 - Random walk with random colour
import random

directions = [0, 90, 180, 270]
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


jim.speed("fastest")
jim.pensize(5)

for _ in range(200):
    jim.color(random_color())
    jim.setheading(random.choice(directions))
    jim.forward(30)
    pass


# Challange 5 - Spirograph

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        jim.circle(100)
        jim.color(random_color())
        jim.setheading(jim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
