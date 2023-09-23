from turtle import Turtle,Screen

MOVE=20
COR = [(0, 0), (-20, 0), (-40, 0),]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):

        self.snake_list=[]
        self.creat_snake()
    def creat_snake(self):
        for position in COR:
            self.add_segment(position)



    def add_segment(self, position):
        snake = Turtle()
        snake.penup()
        snake.color("red")
        snake.shape("square")
        snake.goto(position)
        self.snake_list.append(snake)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())


    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            xc = self.snake_list[i - 1].xcor()
            yc = self.snake_list[i - 1].ycor()
            self.snake_list[i-1].color("red")
            self.snake_list[i].goto(xc, yc)

        self.snake_list[0].forward(MOVE)
        # self.snake_list[0].left(10)


    def listen(self):
        screen = Screen()
        screen.listen(0)
        screen.onkey(key="Up",fun=self.up)
        screen.onkey(key="Down", fun=self.down)
        screen.onkey(key="Right", fun=self.right)
        screen.onkey(key="Left", fun=self.left)

    def up(self):
        if self.snake_list[0].heading()==DOWN:
            pass
        else:
            self.snake_list[0].setheading(UP)
    def down(self):
        if self.snake_list[0].heading() == UP:
            pass
        else:
            self.snake_list[0].setheading(DOWN)


    def left(self):
        if self.snake_list[0].heading() == RIGHT:
            pass
        else:
            self.snake_list[0].setheading(LEFT)
    def right(self):
        if self.snake_list[0].heading() == LEFT:
            pass
        else:
            self.snake_list[0].setheading(RIGHT)