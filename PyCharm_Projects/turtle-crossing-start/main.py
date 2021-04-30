import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def bind_functions(player, screen):

    screen.onkey(player.move_ahead, "Up")

def check_collision(player, car_manager):

    collision = False

    for car in car_manager.cars:
        distance = player.distance(car)
        if distance < 22:
            collision = True
            break

    return collision

if __name__ == "__main__":

    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    screen.listen()

    player = Player()
    score_board = Scoreboard()
    car_manager = CarManager()

    bind_functions(player, screen)
    current_level = 1
    game_is_on = True
    while game_is_on:
        time.sleep(0.3)

        level = player.check_finish_line()
        if current_level != level:
            current_level = level
            score_board.update_level(current_level)
            car_manager.update_level(current_level)

        car_manager.move_cars()
        if check_collision(player, car_manager):
            score_board.game_over()
            game_is_on = False
        screen.update()

    screen.exitonclick()
