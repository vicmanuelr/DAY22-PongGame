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
        x_move = self.xcor() + 14
        y_move = self.ycor() + 10
        self.goto(x_move, y_move)
        time.sleep(0.08)
