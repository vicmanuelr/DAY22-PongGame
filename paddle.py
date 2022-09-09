from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle:

    def __init__(self, coordinates):
        self.paddle = Turtle("square")
        self.paddle.speed("fastest")
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.setheading(UP)
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.goto(coordinates)

    def up(self):
        if not self.wall_limit_up():
            self.paddle.forward(20)

    def down(self):
        if not self.wall_limit_down():
            self.paddle.backward(20)

    def wall_limit_up(self):
        if self.paddle.ycor() > 240:
            return True

    def wall_limit_down(self):
        if self.paddle.ycor() > 240:
            return True
