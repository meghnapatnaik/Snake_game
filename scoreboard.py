from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Arial", 15, "bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(-40, 250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.scores}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.scores > self.high_score:
            self.high_score = self.scores
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")

        self.scores = 0
        self.update_score()

    def increment_score(self):
        self.scores += 1
        self.update_score()
