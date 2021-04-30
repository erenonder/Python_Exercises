from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, color, screen_height, screen_width, size=0.5, shape="circle"):
        super().__init__()
        self.hideturtle()
        self.min_pos_x = -screen_height/2 + 20
        self.max_pos_x = screen_height/2 - 20
        self.min_pos_y = -screen_width/2 + 20
        self.max_pos_y = screen_width/2 - 20

        self.set_new_food_position()

        self.pos_x = 0
        self.pos_y = 0

        self.penup()
        self.speed("fastest")
        self.color(color)
        self.shape(shape)
        self.shapesize(size)
        # self.set_new_food_position()


    def set_new_food_position(self):
        self.pos_x = random.randint(self.min_pos_x, self.max_pos_x)
        self.pos_y = random.randint(self.min_pos_y, self.max_pos_y)
        self.setposition(self.pos_x, self.pos_y)
        self.showturtle()
