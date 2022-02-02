from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fast")
        self.x_move = 10
        self.y_move = 8
        self.penup()
        self.move_speed = 0.1

    def auto(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def stop(self):
        self.goto(0, 0 )
        self.hideturtle()

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.bounce_x()
        self.move_speed = 0.1
        self.goto(0, 0)
