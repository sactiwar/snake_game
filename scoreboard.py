from food import Food

from turtle import Turtle
from food import Food
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(x=0,y=280)
        self.color("orange")
        self.write(f"score {self.score}", align="center",font=("Arial",23,"normal"))
        self.hideturtle()


    def increase_score(self):

        self.score += 1
        self.clear()
        self.write(f"score {self.score}", align="center", font=("Arial", 23, "normal"))

    def game_over(self):
        self.penup()
        self.goto(x=0, y=120)
        self.color("White")
        self.write(f"Your final score is: {self.score}", align="center", font=("Arial", 23, "normal"))
        self.goto(x=0, y=80)
        self.color("White")
        self.write(f" {'GAME OVER'}", align="center", font=("Arial", 23, "normal"))
        self.hideturtle()