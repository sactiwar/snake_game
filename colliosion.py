from turtle import Turtle

class Colliosion(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.right_boundary()
        self.top_boundary()
        self.left_boundary()
        self.bottom_boundary()
    def right_boundary(self):
        self.penup()
        self.goto(x=340,y=340)
        self.pendown()
        self.goto(x=340,y=-340)

    def top_boundary(self):
        self.penup()
        self.goto(x=340, y=340)
        self.pendown()
        self.goto(x=-340, y=340)

    def left_boundary(self):
        self.penup()
        self.goto(x=-340, y=-340)
        self.pendown()
        self.goto(x=-340, y=340)

    def bottom_boundary(self):
        self.penup()
        self.goto(x=-340, y=-340)
        self.pendown()
        self.goto(x=340, y=-340)