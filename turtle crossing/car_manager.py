import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.hideturtle()
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            new_car.showturtle()
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
