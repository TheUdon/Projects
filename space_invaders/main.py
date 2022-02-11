from scoreboard import ScoreBoard
from turtle import Screen
import time
import player
from enemy import Enemy

scoreboard = ScoreBoard()

screen = Screen()

# Will use this code to change how game looks in the future
# # change background pic
# screen.bgpic('./img/battle.gif')
# # add new shapes
# screen.register_shape('./img/tie_small.gif')
# screen.register_shape('./img/jedi_small.gif')
# screen.register_shape('./img/boom.gif')
#
# # now you can use the new shape (e.g. in a class):
# self.ship.shape('./img/tie_small.gif')

screen.setup(width=990, height=1000)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

player = player.Player()
screen.listen()
screen.onkey(player.fire_laser, "space")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

game_on = True

enemy_params = {"y_pos":[200, 240, 280, 320, 360],
               "x_pos":[-205, -165, -125, -85, -45, -5, 35, 75, 115, 155, 195]}

enemies = []

def make_enemies():
    row = 1
    for y in enemy_params["y_pos"]:
        for x in enemy_params["x_pos"]:
            enemies.append(Enemy(x, y))
        row += 1

make_enemies()

print(enemies)

while game_on:
    screen.update()
    time.sleep(.15)

    if scoreboard.lives < 0:
        game_on = False

    player.laser_auto()

    if any(enemy.xcor() < -470 for enemy in enemies):
        for enemy in enemies:
            enemy.setposition(enemy.xcor(), enemy.ycor() - 50)
            enemy.move_direction = "RIGHT"
    elif any(enemy.xcor() > 470 for enemy in enemies):
        for enemy in enemies:
            enemy.setposition(enemy.xcor(), enemy.ycor() - 50)
            enemy.move_direction = "LEFT"

    # Detect laser collision with enemy
    for enemy in enemies:
        enemy.laser_auto()
        enemy.fire_laser()
        try:
            if player.laser.distance(enemy) < 20:
                enemies.remove(enemy)
                player.laser_reset()
                scoreboard.update_score(enemy.score_value)
                enemy.delete()
        except IndexError:
            pass

        if player.ship.distance(enemy.laser) < 20:
            player.reset()
            scoreboard.lives -= 1
            scoreboard.update_board()

        enemy.auto()


screen.exitonclick()
