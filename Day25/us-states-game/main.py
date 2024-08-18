import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
state_data = data["state"].to_list()
guessed_state = []
score = 0


game_is_on = True
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the state", prompt="What's another state's "
                                                                                             "name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_data if state is not guessed_state]
        # for state in state_data:
        #     if state is not guessed_state:
        #         missing_states.append(state)
        #         print(missing_states)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_data:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        right_state = data[data.state == answer_state]
        t.goto(right_state.x.item(), right_state.y.item())
        t.write(right_state.state.item())

# states_to_learn.csv
