import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_state = []
with open("correct.txt", "r+") as f:
    correct = f.read()
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
while len(guessed_state) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_state)}/50 States Correct",prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        not_guessed_state = [state for state in states if state not in guessed_state]
        # for state in states:
        #     if state not in guessed_state:
        #         not_guessed_state.append(state)
        new_data = pd.DataFrame(not_guessed_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)


screen.exitonclick()