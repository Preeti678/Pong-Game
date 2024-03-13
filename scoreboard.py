from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() #to clear the score before the score updates
        self.goto(-200, 250)
        self.write("Player 1 : {}".format(self.l_score), align="center", font=("Courier", 16))
        self.goto(200, 250)
        self.write("Player 2 : {}".format(self.r_score), align="center", font=("Courier", 16))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
