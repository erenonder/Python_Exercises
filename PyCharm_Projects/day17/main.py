from turtle import Turtle, Screen
import random


timmy = Turtle()
timmy.shape("turtle")

screen = Screen()
screen.colormode(255)



# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# for i in range(50):
#     if i % 2 != 0:
#         timmy.penup()
#     else:
#         timmy.pendown()
#     timmy.forward(10)

move_count = 3
color_palette = ["red", "yellow", "green", "black", "orange", "blue", "purple", "brown"]
turn_dir_list = ["right", "left", "none"]
dir_list = ["forward", "backward"]

directions = [0, 90, 180, 270]


def draw_shape(step_number, move_count, color_name):
    timmy.color(color_name)
    for i in range(move_count):
        timmy.forward(step_number)
        timmy.right(360/move_count)

def random_walk(steps):

    timmy.pensize(10)
    timmy.speed(10)
    for i in range(steps):
        timmy.color(random_color())

        timmy.setheading(random.choice(directions))
        timmy.forward(50)



def random_color():

    color = random.sample(range(0, 255), 3)
    return tuple(color)

timmy.speed("fastest")
timmy.pensize(1)
for i in range(36):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)



# random_walk(100)
# for i in range(8):
#     color = random.choice(color_palette)
#     color_palette.remove(color)
#     draw_shape(100, move_count, color)
#     move_count += 1

# print(randomcolor())




# to keep the screen until an action

screen.exitonclick()