
from turtle import Turtle, Screen
import random



def create_turtles(screen_width, turtle_count):
    turtles = []
    turtle_colors = ("red", "green", "blue", "black", "orange")

    pos_x = - (screen_width/2) + 50
    pos_y = -100

    for i in range(turtle_count):

        turtle = Turtle()
        turtle.penup()
        turtle.shape(name="turtle")
        turtle.color(turtle_colors[i])
        turtle.setposition(x=pos_x, y=pos_y)
        pos_y = pos_y + 50
        turtles.append(turtle)

    return turtles

def start_race(turtles, user_bet):

    race_complete = False
    while not race_complete:
        for i in range(len(turtles)):
            pace = random.randint(1,10)
            turtles[i].forward(pace)
            pos_x, pos_y = turtles[i].position()
            # print(f"{turtles[i].color()} position {pos_x}")
            if pos_x >= 400:
                race_complete = True
                winner_turtle = turtles[i].color()[0].lower()
                # print(f"Winner is {turtles[i].color()[0]}")
                if winner_turtle == user_bet:
                    print("You win!")
                else:
                    print(f"You Lose, winner is the {winner_turtle} turle")


if __name__ == "__main__":


    screen = Screen()
    screen_width = 800
    screen.setup(width=screen_width, height=800)
    racing_turtles = create_turtles(screen_width, 5)
    user_bet = screen.textinput("Bet", "Which turtle do you bet on:")
    user_bet = user_bet.lower()
    print(f"User bet {user_bet}")

    start_race(racing_turtles, user_bet)

    screen.exitonclick()
