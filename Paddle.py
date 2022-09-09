from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle:

    def __init__(self):
        self.snake_segments = []
        self.new_snake()
        self.head = self.snake_segments[0]

    def new_snake(self):
        x = (0, 0, 0)
        y = (0, -20, -40)
        positions = zip(x, y)
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            x_cor, y_cor = self.snake_segments[seg_num - 1].xcor(), self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x=x_cor, y=y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def collision_wall(self):
        if self.head.xcor() > 290 or self.head.xcor() < -300:
            return True
        elif self.head.ycor() > 290 or self.head.ycor() < -300:
            return True
