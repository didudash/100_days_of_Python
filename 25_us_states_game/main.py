import turtle
from PIL import Image
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
width, height = Image.open(image).size
screen.addshape(image)
screen.setup(width, height)
turtle.shape(image)

states_df = pd.read_csv("50_states.csv")
all_states = states_df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    if answer_state == "Exit":
        states_to_learn = [item for item in all_states if item not in guessed_states]
        states_to_learn_df = pd.DataFrame(states_to_learn)
        states_to_learn_df.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()  # to not draw path
        state_data = states_df[states_df.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)
