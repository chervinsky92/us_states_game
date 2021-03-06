import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('US States Game')
screen.setup(width=725, height=491)
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

data = pd.read_csv('50_states.csv')
all_states = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f'{len(guessed_states)}/50',
                              prompt='Name a State:').title()
    if answer == 'Exit':
        missed_states = [state for state in all_states if state not in guessed_states]
        series = pd.Series(missed_states, name='Missed States')
        series.to_csv('states_to_learn.csv')
        break

    elif answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        state = data[data.state == answer]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer)
