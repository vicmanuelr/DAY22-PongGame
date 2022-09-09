from turtle import Screen, Turtle
from paddle import Paddle

WIDTH = 800
HEIGHT = 600
RIGHT_PADDLE_COOR = (350, 0)
LEFT_PADDLE_COOR = (-350, 0)

# Initialize instances of screen and paddle
screen = Screen()
right_paddle = Paddle(RIGHT_PADDLE_COOR)
left_paddle = Paddle(LEFT_PADDLE_COOR)

# setup screen and listeners for key press response
screen.setup(width=800, height=600, startx=100, starty=-75)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")


screen.exitonclick()
