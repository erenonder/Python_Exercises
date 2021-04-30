import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800


def detect_collision_with_wall(snake_position):
    collision = False
    # print(snake_position[0])
    # print(SCREEN_WIDTH/2)
    if snake_position[0] > SCREEN_WIDTH/2 - 20 or snake_position[0] < -SCREEN_WIDTH/2 + 20:
        collision = True
    elif snake_position[1] > SCREEN_HEIGHT / 2 - 20 or snake_position[1] < -SCREEN_HEIGHT / 2 + 20:
        collision = True
    else:
        collision = False

    # print(collision)
    return not collision


def detect_collision_with_tail(snake):
    collision = False

    # head_x, head_y = snake.head.position()
    for snake_segment in snake.snake_list[1:]:
        distance = snake_segment.distance(snake.head)
        if distance <= 10:
            collision = True

    return not collision


if __name__ == "__main__":
    snake = Snake(screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH, move_speed=20)
    snake.screen.listen()
    snake.screen.tracer(0)

    food = Food("blue", screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH, size=0.5)
    scoreboard = ScoreBoard(screen_height=SCREEN_HEIGHT)
    game_on = True
    while game_on:
        time.sleep(0.1)
        snake.continue_moving()
        snake.screen.update()

        distance = food.distance(snake.head)
        if distance < 20:
            food.set_new_food_position()
            scoreboard.increase_score()
            snake.add_segment()

        # print(snake.head.position())
        game_on = detect_collision_with_wall(snake.head.position())
        if game_on:
            game_on = detect_collision_with_tail(snake)

    else:
        scoreboard.game_over()



    snake.screen.exitonclick()
