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
        self.paddle.forward(20)

    def down(self):
        self.paddle.backward(20)

    def collision_wall(self):
        if self.head.xcor() > 290 or self.head.xcor() < -300:
            return True
        elif self.head.ycor() > 290 or self.head.ycor() < -300:
            return True
asdf = jaja