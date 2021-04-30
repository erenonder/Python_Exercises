from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time


def setup_screen(screen_obj):

    screen_obj.setup(width=800, height=600)
    screen_obj.bgcolor("black")
    screen_obj.title(titlestring="Pong")
    screen_obj.tracer(n=0)


def bind_right_paddle_functions(screen_obj, paddle_obj):

    screen_obj.onkey(paddle_obj.move_up, "Up")
    screen_obj.onkey(paddle_obj.move_down, "Down")


def bind_left_paddle_functions(screen_obj, paddle_obj):

    screen_obj.onkey(paddle_obj.move_up, "e")
    screen_obj.onkey(paddle_obj.move_down, "s")


def check_ball_paddle_collision(ball_obj, r_paddle_obj, l_paddle_obj):

    coll = False
    paddle_position = "right"
    ball_x, ball_y = ball_obj.pos()

    if ball_x >= 330 and (ball_obj.distance(r_paddle_obj) <= 60):
        coll = True
        paddle_position = "right"
    elif ball_x <= -330 and (ball_obj.distance(l_paddle_obj) <= 60):
        coll = True
        paddle_position = "left"
    else:
        coll = False

    return coll, paddle_position


if __name__ == "__main__":

    screen = Screen()

    setup_screen(screen_obj=screen)

    right_paddle = Paddle("white", 5, 1, 350, 0)
    left_paddle = Paddle("red", 5, 1, -350, 0)

    ball = Ball(ball_width=1.5, ball_height=1.5)
    score_board = ScoreBoard()

    bind_right_paddle_functions(screen_obj=screen, paddle_obj=right_paddle)
    bind_left_paddle_functions(screen_obj=screen, paddle_obj=left_paddle)
    screen.listen()
    game_on = True

    while game_on:
        time.sleep(0.05)
        screen.update()
        ball.move_ball()

        ball_collided_paddle, paddle_position = check_ball_paddle_collision(ball, right_paddle, left_paddle)
        if ball_collided_paddle:
            ball.ball_collided_paddle(paddle_position)
        score, scorer = ball.is_goal_scored()
        if score:
            score_board.update_score(scorer)


    screen.exitonclick()
