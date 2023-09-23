from turtle import Turtle,Screen
import random
SCORE = 0
class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(.5,.5)
        self.color("purple")
        self.speed("fastest")
        self.new_food()


    def new_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)

