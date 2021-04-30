from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, ball_width, ball_height):
        super().__init__()
        self.pos_x = 0
        self.pos_y = 0

        self.x_dir = 1
        self.y_dir = 1

        self.offset = 20

        self.shape("circle")
        self.penup()
        self.color("white")
        self.setposition(x=self.pos_x, y=self.pos_y)
        self.shapesize(stretch_wid=ball_width, stretch_len=ball_height)

    def move_ball(self):
        self.pos_x = self.pos_x + 8 * self.x_dir
        self.pos_y = self.pos_y + 6 * self.y_dir
        # print(self.pos_x)
        self.setposition(x=self.pos_x, y=self.pos_y)
        self.check_wall_collision()

    def check_wall_collision(self):
        pos_x, pos_y = self.position()

        if pos_y >= 300 - self.offset:
            self.y_dir = -1
        elif pos_y <= -300 + self.offset:
            self.y_dir = 1
        else:
            pass

    def ball_collided_paddle(self, padlle_position):

        if padlle_position == "right":
            self.x_dir = -1
        else:
            self.x_dir = 1

    def is_goal_scored(self):

        pos_x, pos_y = self.position()
        score = False
        scorer = ""
        if pos_x >= 400:
            scorer = "left"
            score = True
        elif pos_x <= -400 + self.offset:
            scorer = "right"
            score = True
        else:
            score = False

        if score:
            self.reset_ball_position()

        return score, scorer

    def reset_ball_position(self):

        self.pos_x = 0
        self.pos_y = 0

        self.x_dir = self.x_dir * -1
        self.y_dir = self.y_dir * random.choice([-1, 1])

        self.setposition(x=self.pos_x, y=self.pos_y)



