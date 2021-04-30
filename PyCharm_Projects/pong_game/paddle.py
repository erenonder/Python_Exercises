from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, paddle_color, paddle_width_stretch, paddle_height_stretch, paddle_pos_x, paddle_pos_y):
        super().__init__()
        # self.speed("fastest")
        self.setheading(90)
        self.penup()
        self.color(paddle_color)
        self.shape("square")
        self.shapesize(stretch_wid=paddle_height_stretch, stretch_len=paddle_width_stretch)
        self.setposition(x=paddle_pos_x, y=paddle_pos_y)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)