from re import T
import turtle
import pandas

FONT = ("Courier", 15, "bold")

screen = turtle.Screen()
screen.setup(width=730, height=500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 - Guess the State", "What's another state's name?").title()
    if answer_state == "Exit":
        break
    elif answer_state in states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    
states_to_learn = []
for state in states:
    if state not in guessed_states:
        states_to_learn.append(state)

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")