import turtle


class Snake:

    def __init__(self, screen_width=600, screen_height=600, move_speed=20, initial_length=3):
        self.snake_list = []
        self.screen = turtle.Screen()
        self.screen.setup(width=screen_width, height=screen_height)
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.move_speed = move_speed

        self.create_snake(initial_length)
        self.bind_functions()
        self.head = self.snake_list[0]
        self.directions = {"UP": 90, "DOWN": 270, "RIGHT": 0, "LEFT": 180}

    def continue_moving(self):

        for i in range(len(self.snake_list) - 1, 0, -1):
            desired_position = self.snake_list[i - 1].position()
            self.snake_list[i].setposition(desired_position)
        else:
            self.snake_list[0].forward(self.move_speed)

    def create_snake(self, initial_length=1):

        pos_x = 0
        pos_y = 0
        for i in range(initial_length):
            snake = turtle.Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.speed("fastest")
            snake.setposition(x=pos_x, y=pos_y)
            pos_x = (i + 1) * -self.move_speed
            self.snake_list.append(snake)

    def add_segment(self):
        snake = turtle.Turtle()
        snake.shape("circle")
        snake.color("white")
        snake.penup()
        snake.speed("fastest")
        current_length = len(self.snake_list) + 1
        self.snake_list.append(snake)

    def bind_functions(self):

        turtle.onkeypress(self.move_right, key="Right")
        turtle.onkeypress(self.move_left, key="Left")
        turtle.onkeypress(self.move_up, key="Up")
        turtle.onkeypress(self.move_down, key="Down")

    def move_right(self):
        if self.head.heading() != self.directions["LEFT"]:
            self.head.setheading(self.directions["RIGHT"])

    def move_left(self):
        if self.head.heading() != self.directions["RIGHT"]:
            self.head.setheading(self.directions["LEFT"])

    def move_up(self):
        if self.head.heading() != self.directions["DOWN"]:
            self.head.setheading(self.directions["UP"])

    def move_down(self):
        if self.head.heading() != self.directions["UP"]:
            self.head.setheading(self.directions["DOWN"])
