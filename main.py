import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()
guess_state = []

while len(guess_state) <50:
        ans_state = screen.textinput(title= f"{len(guess_state)}/50 states correct",
                                                        prompt="what's another state name? ")

        if ans_state is None:
            break
        ans_state = ans_state.title()
        if ans_state == "Exit":
            break

        if ans_state in all_state:
            guess_state.append(ans_state)
            t= turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == ans_state]
            t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
            t.write(ans_state)

states_needs_to_learn = []
for state in all_state:
    if state not in guess_state:
        states_needs_to_learn.append(state)
new_data = pd.DataFrame(states_needs_to_learn)
new_data.to_csv("states_needs_to_learn.csv", index=False)