from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1, 1)
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x=coordinate[0], y=coordinate[1])

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
