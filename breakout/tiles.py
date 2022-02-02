from turtle import Turtle
UP = 90


class Tile(Turtle):

    def __init__(self, color, x, y, value):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=2)
        self.color(color)
        self.speed(10)
        self.penup()
        self.setheading(UP)
        self.goto(x, y)
        self.value = value

    def break_tile(self):
        self.hideturtle()