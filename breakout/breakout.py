from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from tiles import Tile
import random as rand

screen = Screen()
wn = screen.getcanvas()

screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)
screen.setup(height=1200, width=1000)

def move_with_mouse(event):
    paddle.move(event.x)

wn.bind('<Motion>', move_with_mouse)

scoreboard = ScoreBoard()

line = Turtle("square")
line.color("white")
line.penup()
line.goto(0, 530)
line.setheading(90)
line.pendown()
line.forward(100)
line.penup()
line.goto(-500, 530)
line.setheading(0)
line.pendown()
line.forward(1100)
line.hideturtle()

paddle = Paddle(-500)
screen.listen()

starting_angle = rand.randint(225, 315)
ball = Ball()

game_on = True

tile_params = {"colors":["blue", "green", "yellow", "orange", "red"],
               "y_pos":[200, 240, 280, 320, 360],
               "x_pos":[-450, -350, -250, -150, -50, 50, 150, 250, 350, 450]}

tiles = []

def make_tiles():
    row = 0
    column = 0
    for y in tile_params["y_pos"]:
        for x in tile_params["x_pos"]:
            tiles.append(Tile(tile_params["colors"][row], x, y, (row + 1)))
        row += 1


make_tiles()

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.auto()

    if scoreboard.lives < 0:
        ball.stop()

    if len(tiles) == 0:
        make_tiles()

    for tile in tiles:
        if ball.distance(tile) < 40:
            ball.bounce_y()
            scoreboard.points(tile.value)
            tiles.remove(tile)
            tile.break_tile()

    if ball.ycor() > 510 or ball.distance(paddle) < 30:
        ball.bounce_y()

    if ball.xcor() < -480 or ball.xcor() > 480:
        ball.bounce_x()

    if ball.ycor() < -500:
        scoreboard.lost_life()
        ball.reset_ball()




screen.exitonclick()
