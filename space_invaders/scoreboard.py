from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        file.close()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.lives = 2
        self.update_board()

    def update_score(self, score_value):
        self.score += score_value
        self.update_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("highscore.txt", mode="w") as file:
            file.write(f"{str(self.high_score)}")
        self.score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-400, 460)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(250,460)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.goto(-400,-480)
        if self.lives < 0:
            self.write(f"Lives: 0", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Lives: {self.lives}", align=ALIGNMENT, font=FONT)
