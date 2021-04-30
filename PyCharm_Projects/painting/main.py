import colorgram
import turtle
import random


def create_color_list():
    # Extract 6 colors from an image.
    colors = colorgram.extract('image.jpg', 40)

    color_list = []

    for color in colors:
        rgb = color.rgb
        # print(rgb)
        color_list.append((rgb.r, rgb.g, rgb.b))

    return color_list

def draw_dots(turtle, color_list=None):

    start_pos_x = -250
    start_pos_y = -250

    turtle.speed("fastest")
    turtle.hideturtle()
    turtle.penup()

    pos_x = start_pos_x
    pos_y = start_pos_y

    for row in range(10):

        turtle.setposition(pos_x, pos_y)

        for column in range(10):

            # turtle.dot(20, color_list[(column * (row+1)) % len(color_list)] )
            turtle.dot(20, random.choice(color_list))

            turtle.penup()

            turtle.forward(50)

        turtle.penup()

        pos_x = start_pos_x
        pos_y = start_pos_y + (row + 1) * 50





if __name__ == "__main__":
    color_list = create_color_list()
    screen = turtle.Screen()
    screen.colormode(255)
    michel = turtle.Turtle()

    draw_dots(michel, color_list)


    screen.exitonclick()