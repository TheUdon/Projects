###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random

colors_to_use = [(251, 250, 247), (84, 84, 83), (202, 217, 238), (34, 33, 33), (162, 165, 180), (14, 16, 22),
                 (244, 211, 219), (242, 169, 188), (187, 127, 144), (86, 90, 97), (32, 18, 25), (102, 82, 91),
                 (187, 172, 156), (251, 253, 253), (177, 191, 212), (82, 85, 83), (22, 24, 23), (212, 190, 165),
                 (150, 113, 134), (60, 61, 73), (79, 54, 64), (121, 125, 141), (152, 155, 153), (69, 64, 55),
                 (133, 128, 119), (224, 179, 173), (87, 53, 51), (153, 117, 116), (161, 200, 216), (60, 66, 62)]


# rgb_colors = []

painter = t.Turtle()

t.colormode(255)
t.mode("standard")
painter.speed("normal")
painter.penup()
painter.hideturtle()
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
# print(rgb_colors)


y = -250
for height in range(10):
    painter.setx(-250)
    painter.sety(y)
    painter.setheading(0)
    for width in range(10):
        color = random.choice(colors_to_use)
        painter.dot(20, color)
        painter.forward(50)
    y += 50


screen = t.Screen()
screen.exitonclick()
#TODO: need 10 by 10 spots
#TODO: dots equal 20 in size
#TODO: dots are spaced by 50