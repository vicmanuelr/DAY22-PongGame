from turtle import Screen
from paddle import Paddle
from ball import Ball

WIDTH = 800
HEIGHT = 600
RIGHT_PADDLE_COOR = (350, 0)
LEFT_PADDLE_COOR = (-350, 0)

# Initialize instances of screen and paddle
screen = Screen()
right_paddle = Paddle(RIGHT_PADDLE_COOR)
left_paddle = Paddle(LEFT_PADDLE_COOR)
ball = Ball()

# setup screen and listeners for key press response
screen.tracer(0)  # Disable screen animation to create paddles
screen.setup(width=WIDTH, height=HEIGHT, startx=100, starty=-75)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()  # works with screen animation
    ball.start_moving()

screen.exitonclick()
