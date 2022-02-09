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
        self.update_board()

    def update_score(self):
        self.score += 10
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
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

