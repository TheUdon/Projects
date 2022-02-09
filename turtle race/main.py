from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Today's racers are red, orange, yellow, green, blue, and purple."
                                   "\nWhich turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

line = Turtle()
line.speed("fastest")
line.hideturtle()
line.penup()
line.goto(230, -200)
line.setheading(90)
line.pendown()
line.forward(510)


def crowd_gen():
    crowd = ""
    x = -240
    y_1 = -170
    heading = 90
    for chunks in range(2):
        for row in range(2):
            for audience in range(16):
                crowd = "crowd" + str(audience)
                crowd = Turtle("turtle", visible=False)
                crowd.speed("fastest")
                crowd.penup()
                crowd.color(random.choice(colors))
                crowd.setheading(heading)
                crowd.goto(x, y_1)
                crowd.showturtle()
                x += 30
            y_1 += 30
            x = -240
        heading = 270
        y_1 = 140
        x = -240



def line_move(y_cord):
    line.penup()
    y_cord = y_cord - 15
    line.goto(-250, y_cord)
    line.setheading(0)
    line.pendown()
    line.forward(500)
    y_cord = y_cord + 30
    line.penup()
    line.goto(-250, y_cord)
    line.setheading(0)
    line.pendown()
    line.forward(500)

y = -75

for c in colors:
    color = c
    color = Turtle("turtle")
    color.penup()
    color.color(c)
    color.goto(-240, y)
    line_move(y)
    y += 30
    all_turtle.append(color)

if user_bet:
    race_on = True

crowd_gen()

while race_on is True:
    for racer in all_turtle:
        if racer.xcor() > 230:
            race_on = False
            winner = racer.pencolor()
            if winner == user_bet.lower():
                print(f"You've won! The winner was the {winner} turtle!")
            else:
                print(f"You've lost! The winner was the {winner} turtle!")
        distance = random.randint(0, 10)
        racer.forward(distance)


screen.exitonclick()