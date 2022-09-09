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
        """Movement of paddle up with wall limit"""
        if not self.paddle.ycor() > 240:
            self.paddle.forward(20)

    def down(self):
        """Method for movement of paddle down with wall limt"""
        if not self.paddle.ycor() < -240:
            self.paddle.backward(20)
