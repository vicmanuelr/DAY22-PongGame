from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
RIGHT_PADDLE_COOR = (350, 0)
LEFT_PADDLE_COOR = (-350, 0)

# Initialize instances of screen and paddle
screen = Screen()
right_paddle = Paddle(RIGHT_PADDLE_COOR)
left_paddle = Paddle(LEFT_PADDLE_COOR)
ball = Ball()
scoreboard = Scoreboard()

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
    # Wall bounce conditions for ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    # Paddle bounce conditions for ball
    if ball.distance(right_paddle.position()) < 50 and ball.xcor() > 335 or ball.distance(
            left_paddle.position()) < 50 and ball.xcor() < -335:
        ball.paddle_bounce()
    # Conditions of ball off the board/table/screen
    if ball.xcor() > 380:
        ball.ball_restart()
        scoreboard.left_point()
    elif ball.xcor() < -380:
        ball.ball_restart()
        scoreboard.right_point()

screen.exitonclick()
