from random import randint
from turtle import Turtle
STARTING = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Enemy(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.score_value = 10
        self.speed("slow")
        self.penup()
        self.setheading(UP)
        self.goto(x, y)
        self.move_direction = "RIGHT"
        self.laser = Turtle("triangle")
        self.laser.color("red")
        self.laser.hideturtle()
        self.laser.setheading(DOWN)
        self.laser.shapesize(0.5, 0.5)
        self.laser.penup()
        self.laser_state = "READY"

    def auto(self):
        if self.move_direction == "RIGHT":
            x = self.xcor()
            x += 10
            self.goto(x, self.ycor())
        elif self.move_direction == "LEFT":
            x = self.xcor()
            x -= 10
            self.goto(x, self.ycor())

    def fire_laser(self):
        chance_to_fire = randint(0, 8000)
        if chance_to_fire > 7950:
            if self.laser_state == "READY":
                self.laser.setposition(self.xcor(), self.ycor() - 10)
                self.laser.showturtle()
                self.laser_state = "FIRE"

    def laser_auto(self):
        if self.laser_state == "FIRE":
            self.laser.forward(20)
            if self.laser.ycor() < -370:
                self.laser.setposition(self.xcor(), self.ycor() - 10)
                self.laser.hideturtle()
                self.laser_state = "READY"


    def delete(self):
        self.hideturtle()
        self.score_value = 0
