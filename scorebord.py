from turtle import Turtle
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("White")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}\nHigh Score: {self.high_score}", align="center", font=FONT)
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}\nHigh Score: {self.high_score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

