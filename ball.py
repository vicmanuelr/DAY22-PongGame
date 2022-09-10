from turtle import Turtle
import time
INITIAL_POSITION = (0, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self. shape("circle")
        self.penup()
        self.speed("slowest")

    def start_moving(self):
        self.setheading(36.87)
        self.forward(20)
        time.sleep(0.1)

