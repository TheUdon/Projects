from turtle import Turtle
STARTING = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player:

    def __init__(self):
        self.ship = Turtle("square")
        self.ship.color("green")
        self.ship.speed("normal")
        self.ship.penup()
        self.ship.goto(-5, -350)
        self.laser = Turtle("triangle")
        self.laser.color("yellow")
        self.laser.hideturtle()
        self.laser.setheading(UP)
        self.laser.shapesize(0.5, 0.5)
        self.laser.penup()
        self.laser_state = "READY"

    def fire_laser(self):
        if self.laser_state == "READY":
            self.laser.setposition(self.ship.xcor(), self.ship.ycor() + 10)
            self.laser.showturtle()
            self.laser_state = "FIRE"

    def laser_auto(self):
        if self.laser_state == "FIRE":
            self.laser.forward(20)
            if self.laser.ycor() > 360:
                self.laser.hideturtle()
                self.laser_state = "READY"

    def laser_reset(self):
        self.laser.setposition(self.ship.xcor(), self.ship.ycor() + 10)
        self.laser_state = "READY"
        self.laser.hideturtle()

    def left(self):
        x = self.ship.xcor()
        x -= 20
        if x < -500:
            pass
        else:
            self.ship.setx(x)

    def right(self):
        x = self.ship.xcor()
        x += 20
        if x > 500:
            pass
        else:
            self.ship.setx(x)

    def reset(self):
        self.ship.clear()
        self.ship.goto(-5, -350)
