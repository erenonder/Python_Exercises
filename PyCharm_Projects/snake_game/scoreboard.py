from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.file_name = "snake_high_score.txt"
        self.high_score = 0
        self.penup()
        self.check_high_score()
        self.setposition(-20, screen_height/2 - 30)
        self.update_score_board()

    def check_high_score(self):
        file_exists = os.path.exists(self.file_name)

        try:
            if file_exists:
                with open(self.file_name, 'r') as high_score_file:
                    read_score = high_score_file.read()
                    self.high_score = int(read_score)
            else:
                with open(self.file_name, 'w') as high_score_file:
                    high_score_file.write(f"{self.high_score}")
        except ValueError:
            print("High Score File could not be read")

    def update_score_board(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        print(f"score: {self.score} high: {self.high_score}")
        if self.score > self.high_score:
            with open(self.file_name, 'w') as high_score_file:
                high_score_file.write(f"{self.score}")

        self.setposition(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):

        self.score += 1
        self.clear()
        self.update_score_board()
