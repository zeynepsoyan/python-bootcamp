# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g,b))

# print(rgb_colors)

import turtle as t
import random

jim = t.Turtle()
t.colormode(255)
jim.speed("fastest")
jim.hideturtle()
jim.penup()

color_list = [(201, 164, 112), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

jim.setheading(225)
jim.forward(350)
jim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    jim.dot(20, random.choice(color_list))
    jim.forward(50)

    if dot_count % 10 == 0:
        jim.setheading(90)
        jim.forward(50)
        jim.setheading(180)
        jim.forward(500)
        jim.setheading(0)


screen = t.Screen()
screen.exitonclick()