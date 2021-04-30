from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-220, 260)


class Scoreboard():

    def __init__(self, level=1):

        self.level_print = Turtle()

        self.game_over_print = Turtle()
        self.game_over_print.penup()
        self.game_over_print.hideturtle()

        self.level_print.level = level
        self.level_print.penup()
        self.level_print.hideturtle()
        self.level_print.color("black")
        self.level_print.setposition(POSITION)
        self.level_print.write(f"Level: {self.level_print.level} ", False, align="center", font=FONT)

    def update_level(self, level_to_update):

        if self.level_print.level != level_to_update:
            self.level_print.clear()
            self.level_print.level = level_to_update
            self.level_print.write(f"Level: {self.level_print.level} ", False, align="center", font=FONT)
        else:
            pass

    def game_over(self):
        self.game_over_print.color("black")
        self.game_over_print.setposition(-30, 0)
        self.game_over_print.write(f"GAME OVER", False, align="center", font=("Courier", 36, "normal"))

        # self.write(f"GAME OVER", False, align="center", font=FONT)


