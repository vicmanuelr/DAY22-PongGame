from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600, startx=100, starty=-25)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen. listen()

screen.exitonclick()