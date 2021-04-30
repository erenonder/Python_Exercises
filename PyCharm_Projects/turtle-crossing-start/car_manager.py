from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self, screen_width=600, screen_height=600, car_count=100):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT
        self.level = 1
        self.cars = list()
        self.coordinates = []
        self.car_count = car_count
        self.screen_width = screen_width
        self.create_cars()

    def create_cars(self):
        self.create_random_coordinates()
        for car_index in range(self.car_count):
            self.cars.append(Turtle())
            self.cars[car_index].penup()
            self.cars[car_index].shape("square")
            self.cars[car_index].setposition(self.coordinates[car_index][0], self.coordinates[car_index][1])
            self.cars[car_index].color(random.choice(COLORS))
            self.cars[car_index].setheading(180)
            self.cars[car_index].turtlesize(stretch_wid=1, stretch_len=2)

    def update_cars(self):

        self.update_coordinates()
        for car_index in range(self.car_count):
            self.cars[car_index].setposition(self.coordinates[car_index][0], self.coordinates[car_index][1])
            self.cars[car_index].color(random.choice(COLORS))
            self.cars[car_index].setheading(180)
            self.cars[car_index].turtlesize(stretch_wid=1, stretch_len=2)

    def update_level(self, new_level):

        self.level = new_level
        self.update_cars()

    def create_random_coordinates(self):

        for _ in range(self.car_count):
            pos_y = random.randint(-260, 260)
            pos_x = random.randint(100, self.screen_width/2 + 2000)
            self.coordinates.append((pos_x, pos_y))

    def update_coordinates(self):

        for coordinate_index in range(self.car_count):
            pos_y = random.randint(-260, 260)
            pos_x = random.randint(100, self.screen_width/2 + 2000)
            self.coordinates[coordinate_index] = (pos_x, pos_y)

    def move_cars(self):

        for car_index in range(self.car_count):
            self.cars[car_index].forward(self.move_speed + self.move_increment * self.level - 1)



