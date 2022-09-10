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
        self.x_move = 10
        self.y_move = 10

    def start_moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        time.sleep(0.08)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def ball_restart(self):
        self.goto(0, 0)
        self.x_move *= -1

