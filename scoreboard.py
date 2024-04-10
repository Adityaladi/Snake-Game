from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("../../Desktop/highscore.txt") as hs:
            high_score = hs.read()
        self.score = 0
        self.highscore = int(high_score)
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score = {self.score} Highscore = {self.highscore}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("../../Desktop/highscore.txt", mode="w") as hs:
                hs.write(str(self.highscore))
        self.write(f"Score = {self.score} Highscore = {self.highscore}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
