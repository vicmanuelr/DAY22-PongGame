from turtle import Screen, Turtle
UP = 90
DOWN = 270


screen = Screen()
screen.setup(width=800, height=600, startx=100, starty=-75)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


right_paddle = Turtle("square")
right_paddle.penup()
right_paddle.speed("slow")
right_paddle.color("white")
right_paddle.setheading(90)
right_paddle.shapesize(stretch_wid=1, stretch_len=5)
right_paddle.goto(350, 0)


right_paddle.forward(20)




screen.exitonclick()
