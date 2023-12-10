import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        # Detect collision with car
        if player.distance(car) < 20:
            scoreboard.game_over()
            time.sleep(0.3)
            game_is_on = False

    # Detect when turtle was successful
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level += 1
        scoreboard.update_scoreboard()


screen.exitonclick()
