from turtle import Turtle
INITIAL_POSITION = (0, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self. shape("circle")