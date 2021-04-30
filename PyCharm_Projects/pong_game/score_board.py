from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.color("blue")
        self.setposition(-20, 200)
        self.write(f"{self.right_score}       -       {self.left_score}", False, align="center", font=("Arial", 60, "normal"))
        self.penup()

    def update_score(self, scorer):
        if scorer == "right":
            self.right_score += 1
        elif scorer == "left":
            self.left_score += 1
        else:
            pass

        self.clear()
        self.write(f"{self.right_score}       -       {self.left_score}", False, align="center", font=("Arial", 60, "normal"))
