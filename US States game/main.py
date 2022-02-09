import turtle

import pandas
from turtle import Turtle, Screen

data = pandas.read_csv("./50_states.csv")
states = data["state"]
state_list = states.to_list()
writer = Turtle()
writer.penup()
writer.hideturtle()

screen = Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to get the coordinates of the states
# def get_mouse_click_coor(x,y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


def write_state(input):
    state_coor = data[data.state == input]
    writer.goto(int(state_coor.x), int(state_coor.y))
    writer.write(f"{input}", align="center", font=("Courier", 8, "normal"))


correct_guesses = 0
guessed_states = []
missing_states_list = []

game_on = True

while game_on:
    user_answer = screen.textinput(title=f"Guess the State {correct_guesses}/50", prompt="Name one of the States:")
    answer = user_answer.title()
    if answer == "Exit":
        missing_states_list = [state for state in state_list if state not in guessed_states]
        missing_states = pandas.DataFrame(missing_states_list)
        missing_states.to_csv("missing_states.csv")
        game_on = False
    if answer in guessed_states:
        pass
    elif answer in state_list:
        write_state(answer)
        correct_guesses += 1
        guessed_states.append(answer)
    if correct_guesses == 50:
        game_on = False

screen.exitonclick()
