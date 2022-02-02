from turtle import Turtle
UP = 90


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed(10)
        self.penup()
        self.setheading(UP)
        self.yposition = position
        self.goto(0, self.yposition)

    def move(self, xposition):
        if xposition == 500:
            xposition = 0
        elif xposition > 500 or xposition < 500:
            xposition -= 500
            if xposition < -440:
                xposition = -445
            elif xposition > 440:
                xposition = 440
        self.goto(xposition, self.yposition)
