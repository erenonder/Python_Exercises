from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.level = 1
        self.pos_x, self.pos_y = STARTING_POSITION

        self.setposition(STARTING_POSITION)
        self.color("black")

    def move_ahead(self):

        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.setposition(STARTING_POSITION)

    def check_finish_line(self):

        self.pos_x, self.pos_y = self.position()

        if self.pos_y >= FINISH_LINE_Y:
            self.level += 1
            self.reset_position()

        return self.level
