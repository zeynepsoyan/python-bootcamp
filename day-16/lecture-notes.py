# Procedural Programming: Functions
# vs Object Oriented Programming: Classes

# attribute: varibles that are attached to an object (has)
# methods: functions that are attached to an object (does)
# We can generate multiple objects of the same type (blueprint) = class

from turtle import Turtle, Screen

jimmy = Turtle()
print(jimmy)
jimmy.shape("turtle")
jimmy.color("aquamarine3")
jimmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()

# Pretty Table

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)