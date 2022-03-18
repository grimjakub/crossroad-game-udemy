import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
score_board=ScoreBoard()

screen.listen()
screen.onkey(player.move,"Up")
screen.onkey(player.move," ")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()
    car_manager.generate_new_car()

    #detect collision with car
    for car in car_manager.cars:
        if player.distance(car)<20:
            game_is_on=False
            score_board.game_over()
    if player.ycor()>250:
        player.new_level()
        score_board.level_up()
        car_manager.speed_up()

screen.exitonclick()