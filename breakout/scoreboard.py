from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 35, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.lives = 3
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-350, 540)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(250, 540)
        if self.lives < 0:
            self.write("Game Over", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Lives Left: {self.lives}", align=ALIGNMENT, font=FONT)

    def points(self, tile_value):
        self.score += tile_value
        self.write_score()

    def lost_life(self):
        self.lives -= 1
        self.write_score()
